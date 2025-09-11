#! /usr/bin/env python
# -*- coding: utf-8 -*-

# total mess that need full rewrite in sane mind

import os, json

from sys import exit
from datetime import datetime
from time import gmtime, strftime
from os import makedirs
from os.path import join
from shutil import copy
from itertools import chain

from pathlib import Path as path

from core import load_distros, list_distros, build, find_by_id, rq
from log import log, color

from config import config
from shared import ns

if __name__ == '__main__':

    timer = lambda: datetime.now().timestamp()

    timer_start = timer()

    banner = path(join(config.paths.root, 'banner.ascii')).read_text()
    print(color(banner, 'white', attrs=['bold']))

    distros = load_distros(list_distros())
    ids = list(distros.keys())
    total = len(ids)

    log.custom.sys(f'initialized {color(total, 'yellow')} scraper' + ('s' if total > 1 else ''))

    content = []

    included = []
    excluded = []
    outdated = []

    update = list(chain.from_iterable(config.args.update))

    try:
        os.makedirs(join(config.paths.output, 'logos'), exist_ok=True)

        if config.args.fallback:
            try:
                fallback_json = rq.get(config.args.fallback).json()
            except:
                log.custom.sys('failed to load fallback json', 'warning')
                config.args.fallback = None

        for distro in distros.items():
            values = []
            id, module = distro
            info = ns(id=id, **vars(module.info))

            try:
                try:
                    if not id in update and config.args.fallback:
                        releases = find_by_id(fallback_json, id)
                        values = build.entry(distro, releases)
                        log.custom.distro(id, ids, 'used cached values')
                    else:
                        log.custom.distro(id, ids, 'scraping')
                        values = build.entry(distro)
                    
                    if not values['releases']:
                        raise Exception('no urls found')

                    included.append(info)
                    content.append(values)
                    
                    if not update: 
                        log.custom.distro(id, ids, 'scraped')
                
                except Exception as error:
                    if config.args.fallback:
                        try:
                            releases = find_by_id(fallback_json, id)
                            values = build.entry(distro, releases)
                            included.append(info)
                            outdated.append(info)
                            content.append(values)
                            log.warning(log.fmt.distro(id, ids, 'cached values used'))
                        except:
                            log.error(log.fmt.distro(id, ids, error))
                            raise Exception(log.fmt.distro(id, ids, 'cached values not found'))
                    else:
                        raise Exception(log.fmt.distro(id, ids, error))
                
            except Exception as error:
                log.error(error)
                excluded.append(info)
            finally:
                copy(join(config.paths.input, id, 'logo.png'),
                     join(config.paths.output, 'logos', f'{id}.png'))

        if not included:
            log.custom.sys('all scrapers failed', 'critical')
            exit(1)
        else:
            result = []
            if included: result.append(f'{color(len(included), 'yellow')} included')
            if outdated: result.append(f'{color(len(outdated), 'yellow')} outdated')
            if excluded: result.append(f'{color(len(excluded), 'yellow')} excluded')

            format = lambda a, m: log.custom.sys(f'{m} [{color(len(a), 'yellow')}] ' + ', '.join([color(x.id, 'cyan') for x in a]))
            
            if included: format(included, 'included')
            if outdated: format(outdated, 'outdated')
            if excluded: format(excluded, 'excluded')

        status = ns(
            build_time=round(timer() - timer_start),
            last_update=datetime.now().isoformat(),
            distros=ns(
                total=len(included) + len(excluded),
                included=included,
                outdated=outdated,
                excluded=excluded,
            ),
        )

        content.insert(0, build.meta(status))

        with open(join(config.paths.output, 'repo.json'), 'w') as target:
            json.dump(content, target, indent=4, default=lambda x: x.__dict__)

        if config.args.html:
            build.html(status)
            log.custom.sys('html built')

        log.custom.sys('finish!')


    except KeyboardInterrupt:
        exit(130)

    except Exception as error:
        log.critical(str(error).lower(), exc_info=True)
        exit(2)
