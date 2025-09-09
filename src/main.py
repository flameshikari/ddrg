#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, json

from sys import exit
from datetime import datetime
from time import gmtime, strftime
from os import makedirs
from os.path import join
from shutil import copy

from pathlib import Path as path

from core import load_distros, list_distros, build
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

    log.custom.sys(f'loaded {color(total, 'yellow')} distro' + ('s' if total > 1 else ''))

    content = []

    included = []
    excluded = []
    outdated = []

    try:
        os.makedirs(join(config.paths.output, 'logos'), exist_ok=True)
        for distro in distros.items():
            id, module = distro
            info = ns(id=id, **vars(module.info))
            try:
                log.custom.distro(id, ids, 'scraping', 'debug')
                content.append(build.entry(distro))
                copy(join(config.paths.input, id, 'logo.png'),
                     join(config.paths.output, 'logos', f'{id}.png'))
                included.append(info)
                log.custom.distro(id, ids, 'scraped')
            except Exception as error:
                log.exception(error)
                excluded.append(info)

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

    except KeyboardInterrupt:
        exit(130)

    except Exception as error:
        log.critical(str(error).lower(), exc_info=True)
        exit(2)
