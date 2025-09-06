#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json, logging, os, re

from argparse import ArgumentParser

from importlib.machinery import SourceFileLoader
from shutil import copy, copytree, rmtree
from sys import exit
from time import gmtime, sleep, strftime
from itertools import chain
from datetime import datetime
from pathlib import Path as path

try:
    from requests.exceptions import RequestException
    from markdown2 import markdown
    from termcolor import colored as color
    from natsort import natsorted

except ImportError as error:
    print(f"{error}. Did you install packages from requirements.txt?")
    exit(1)


clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
timer = lambda: datetime.now().timestamp()



# setting the workdir to the folder where this script is located
workdir = os.path.dirname(os.path.abspath(__file__))

# parsing arguments passed to this script
parser = ArgumentParser()
parser.add_argument('-d', '--distros', default=[], action='append', metavar='NAME', nargs='+', help='define distros to scrape')
parser.add_argument('-e', '--exclude', default=[], action='append', metavar='NAME', nargs='+', help='exclude distros')
parser.add_argument('-H', '--html', default=False, action='store_true', help='generate html')
parser.add_argument('-f', '--fallback', default=False, action='store_true', help='gather urls from predefined json for failed distros')
parser.add_argument('-l', '--list', default=False, action='store_true', help='show available distros')
parser.add_argument('-i', '--input', default=f'{workdir}/distros', type=str, help='the dir with distros for parsing')
parser.add_argument('-o', '--output', default=f'{workdir}/../repo', type=str, help='the dir for saving builded repo')
parser.add_argument('-v', '--verbose', default=False, action='store_true', help='show more info when scraping distros')

options = parser.parse_args()


# setting other directories
output_dir = os.path.abspath(options.output)
distros_dir = os.path.abspath(options.input)

def configure_logging():
    # logging.getLogger("urllib3").setLevel(logging.DEBUG if options.verbose else logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.addLevelName(logging.DEBUG, color('verb', 'magenta'))
    logging.addLevelName(logging.INFO, color('info', 'blue'))
    logging.addLevelName(logging.WARNING, color('warn', 'yellow'))
    logging.addLevelName(logging.ERROR, color('fail', 'red'))
    logging.addLevelName(logging.CRITICAL, color('crit', 'red'))

    logging.basicConfig(level=logging.DEBUG if options.verbose else logging.INFO,
                        format=f'{color("%(asctime)s", 'dark_grey')} [%(levelname)s] %(message)s',
                        datefmt='%H:%M:%S')


def list_distros(local = True):
    distros = os.listdir(distros_dir)
    if options.distros and not options.list:
        distros = list(chain.from_iterable(options.distros))
    if options.exclude:
        exclude = list(chain.from_iterable(options.exclude))
        distros = [x for x in distros if x not in exclude]
    distros = sorted([distro for distro in distros if not distro.startswith('_')])
    return distros

if options.list:
    distros_list = list_distros()
    if len(distros_list) == 0:
        exit(1)
    else:
        print('\n'.join(distros_list))
        exit(0)

def load_distros(distros):
    modules = {}

    for distro in distros:
        target_dir = f'{distros_dir}/{distro}'

        if not path(target_dir).is_dir():
            logging.error(f"{color(distro, 'yellow', attrs=['underline'])}: distro not found")
            continue
        else:
            if not os.path.exists(f'{target_dir}/scraper.py'):
                logging.error(f"{color(distro, 'yellow', attrs=['underline'])}: scraper not found")
                continue

            if not os.path.exists(f'{target_dir}/logo.png'):
                logging.error(f"{color(distro, 'yellow', attrs=['underline'])}: logo not found")
                continue

        try:
            modules[distro] = SourceFileLoader(distro, f'{target_dir}/scraper.py').load_module()

        except Exception as error:
            logging.error(f"{color(distro, 'yellow', attrs=['underline'])}: {error}")
            continue

    return modules


def find_by_id(json_array, target_id):
    filtered = list(filter(lambda item: item.get('id') == target_id, json_array))
    return filtered[0] if filtered else None




def build_repo_entry(id):
    """Create a tulpe with distro values then return it."""

    tries = 3
    wait = 5

    scraper = distros[id]

    entry = {
        'id': id,
        'name': distros[id].info['name'],
        'url': distros[id].info['url'],
        'releases': []
    }

    distro_values = []

    for i in range(tries):
        try:
            distro_values = natsorted(scraper.init(), key=lambda x: x[3], reverse=True)
        # except requests.exceptions.RequestException as error:
        except RequestException as error:
            if i < tries - 1: # i is zero indexed
                logging.warning(f"{id}: retrying in {wait}s")
                sleep(wait)
                continue
            else:
                if options.fallback:
                    try:
                        values = find_by_id(current_json, id)['releases']
                        distro_values = [
                            values['url'],
                            values.get('arch'),
                            values['size'],
                            values['version']
                        ]
                        break
                    except:
                        raise Exception(f'cannot find {id} in cached json')
                else:
                    raise Exception(f'failed after {tries} tries')
        break

    for distro_value in distro_values:
        iso_url, iso_arch, iso_size, iso_version = distro_value
        a =  {"size": iso_size,
              "url": iso_url,
              "version": iso_version}
        if iso_arch is not None: a['arch'] = iso_arch
        entry['releases'].append(dict(sorted(a.items())))


    if not entry['releases']:
        # logging.error(f"{distro_id}: no releases")
        # return
        raise Exception('releases is empty')

    return entry


def build_repo_html():

    markdown_distros = []
    content_json = {
        'contains': [],
        'missing': [],
    }

    markdown_distros_done = [x for x in distros if (x not in distros_errors)]
    markdown_distros_error = [x for x in distros_errors]

    with open(f"{output_dir}/repo.json", "r") as file:
        repo_json = file.read()

    with open(f"{workdir}/website/body.md", "r") as file:
        markdown_source = file.read()

    for id in markdown_distros_done:
        info = distros[id].info
        markdown_distros.append(f'<a href="{info['url']}"><img title="{info['name']}" loading="lazy" class="distro_logo" src="./logos/{id}.png"/></a>')
        content_json['contains'].append({
            "id": id,
            **info
        })

    markdown_distro_count = f'contains [{len(markdown_distros_done)}](./content.json)'

    if markdown_distros_error:
        for id in markdown_distros_error:
            info = distros[id].info
            content_json['missing'].append({"id": id, **info})
        markdown_distro_count += f' and missing [{len(markdown_distros_error)}](./content.json)'

    markdown_formatted = markdown_source.format(
        count=markdown_distro_count,
        time=strftime('%Y.%m.%d %H:%M:%S'),
        timezone=strftime('%z')[:-2],
        distros="\n".join(markdown_distros))

    markdown_converted = markdown(markdown_formatted)

    with open(f"{workdir}/website/template.html", "r") as file:
        html_template = file.read()

    with open(f"{output_dir}/content.json", "w") as file:
        file.write(json.dumps(content_json, indent=2))

    with open(f"{output_dir}/index.html", "w") as file:
        file.write(html_template.format(body=markdown_converted))

    html_assets_dir = f'{workdir}/website/root/'
    copytree(html_assets_dir, output_dir, dirs_exist_ok=True)






if __name__ == '__main__':

    timer_start = timer()

    from helpers import rq, generate_status_entry


    logo = path(f'{workdir}/logo.txt').read_text()
    print(color(logo, 'white', attrs=['bold']))


    configure_logging()


    distros = load_distros(list_distros())

    if len(distros) == 0:
        logging.critical('no distros loaded')
        exit(1)

    # initialization of arrays
    repo, distros_errors = [], []


    if options.fallback:
        current_json = rq.get('https://dd.hexed.pw/repo.json').json()

    try:
        logging.info(f'loaded {len(distros)} distros')
        items = list(distros.keys())
        for distro in distros:
            try:
                total = f'[{"{:0>{}}".format(items.index(distro) + 1, len(str(len(distros) + 1)))}/{len(distros)}]'
                logging.info(f"{total} {color(distro, 'yellow', attrs=['underline'])} > scraping")
                entry = build_repo_entry(distro)
                repo.append(entry)
                logging.info(f"{total} {color(distro, 'yellow', attrs=['underline'])} > scraped")

            except Exception as error:
                distros_errors.append(distro)
                logging.exception((f"{error}"))
                continue

        timer_stop = round(timer() - timer_start)
        build_time = strftime('%H:%M:%S', gmtime(timer_stop))

        if len(distros_errors) == len(distros):
            logging.critical('the repository is empty')
            exit(2)

        # remove previous output folder structure
        if os.path.exists(f"{output_dir}/repo.json"):
            rmtree(output_dir)

        # create output folder structure
        os.makedirs(f"{output_dir}/logos", exist_ok=True)


        repo.insert(0, generate_status_entry(distros, distros_errors, build_time))

        # create repo.json in output folder
        with open(f'{output_dir}/repo.json', 'w') as target:
            json.dump(repo, target, indent=2)

        # copy distro logos to distro folders
        for distro in distros:
            logo_src = f'{distros_dir}/{distro}/logo.png'
            logo_dst = f'{output_dir}/logos/{distro}.png'
            copy(logo_src, logo_dst)


        if options.html:
            build_repo_html()

        if distros_errors:
            logging.warning(f"not included: {', '.join(distros_errors)}")

        logging.info(f"done! build time: {build_time}")

        exit(0)

    except KeyboardInterrupt:
        exit(130)

    except Exception as error:
        logging.critical(str(error).lower(), exc_info=True)
        exit(2)
