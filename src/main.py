#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os
import re

from argparse import ArgumentParser
from datetime import datetime
from html import unescape
from importlib.machinery import SourceFileLoader
from random import choice
from secrets import token_hex as random_hex
from shutil import copy, copytree, rmtree
from sys import exit
from time import gmtime, sleep, strftime

try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from fake_useragent import UserAgent
    from markdown2 import markdown
    from packaging.version import Version as check_version
    from termcolor import colored as color
    from xmltodict import parse as xml_to_dict

except ImportError as error:
    print(f"{error}. Did you install packages from requirements.txt?")
    exit(1)


clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


# initialization of a timer to count the script execution time
timer = lambda: datetime.now().timestamp()
timer_start = timer()

# setting the workdir to the folder where this script is located
working_dir = os.path.dirname(os.path.abspath(__file__))

# parsing arguments passed to this script
options = ArgumentParser()
options.add_argument("-c", "--color",
                     help="enable color output",
                     default=False,
                     action="store_true")
options.add_argument("-d", "--distros",
                     help="define specific distros to parse",
                     default='all',
                     type=str)
options.add_argument("-g", "--generate",
                     help="generate a webpage to present the content of repo.json",
                     default=False,
                     action="store_true")
options.add_argument("-i", "--input",
                     help="the dir with distros for parsing",
                     default=f"{working_dir}/distros",
                     type=str)
options.add_argument("-o", "--output",
                     help="the dir for saving builded repo",
                     default=f"{working_dir}/../repo",
                     type=str)
options.add_argument("-v", "--verbose",
                     help="show debug info",
                     default=False,
                     action="store_true")
options = options.parse_args()

if options.verbose: level_log = logging.DEBUG
else: level_log = logging.INFO

logging.getLogger("urllib3").setLevel(logging.WARNING)



if options.color:
    logging.addLevelName(logging.DEBUG, color(logging.getLevelName(logging.DEBUG), 'magenta'))
    logging.addLevelName(logging.INFO, color(logging.getLevelName(logging.INFO), 'blue'))
    logging.addLevelName(logging.WARNING, color(logging.getLevelName(logging.WARNING), 'yellow'))
    logging.addLevelName(logging.ERROR, color(logging.getLevelName(logging.ERROR), 'red'))
    logging.addLevelName(logging.CRITICAL, color(logging.getLevelName(logging.CRITICAL), 'red'))
else:
    # replace colored function to print
    def color(text, *args, **kwargs):
        return text

logging.basicConfig(level=level_log,
                    format='[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt='%H:%M:%S')


# setting other directories
output_dir = os.path.abspath(options.output)
distros_dir = os.path.abspath(options.input)

# initialization of arrays
repo, distros_errors = [], []


if options.distros == 'all':
    distros_list = sorted([distro for distro in os.listdir(distros_dir)
                           if not distro.startswith("_")])
else:
    distros_list = sorted(options.distros.split(','))


# https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
DEFAULT_TIMEOUT = 10 # seconds
class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)
retries = Retry(total=3, status_forcelist=[429, 500, 502, 503, 504])
rq = requests.Session()

rq.mount("http://",  TimeoutHTTPAdapter(max_retries=retries))
rq.mount("https://", TimeoutHTTPAdapter(max_retries=retries))

class get:

    def size(target):
        """Returns the file size of the target URL in bytes."""
        try:
            response = rq.get(target, stream=True).headers
            # logging.debug(f"{color(response, 'green')}")
            size = int(response['Content-Length'])
            if size > 500:
                return size
            else:
                return 0
        except Exception as error:
            logging.debug(f"{color('-', 'red')} {target}: {str(error).lower()}")
            pass

    def arch(target):
        """Returns the used processor architecture of the target URL."""

        archs = [
            "amd64", "i386", "86_64"
            "arm64", "arm32", "armhfp", "armhf", "armv7", "armel", "aarch64",
            "i486", "i586", "i686-pae", "i686", "ia64",
            "macppc", "ppc64le", "ppc64el", "ppc64", "ppcspe", "ppc",
            "mips64el", "mipsel", "mips",
            "s390x", "hppa", "alpha", "sparc64",
            "bios", "efi", "ipxe"
        ]

        archs_86_64 = ["86-64", "96"]
        archs_64 = ["x64", "64bit", "dual", "64"]
        archs_86 = ["x86", "x32", "32bit", "386", "32"]

        for arch in archs:
            if arch in target:
                return arch

        if any(arch in target for arch in archs_86_64):
            return "x86_64"

        elif any(arch in target for arch in archs_64):
            return "amd64"

        elif any(arch in target for arch in archs_86):
            return "i386"

        elif "powerpc" in target:
            for ppc in archs:
                if ppc in target.replace("powerpc", "ppc"):
                    return ppc

        elif "legacy" in target:
            return "bios"

        else:
            return None


    def urls(target, **kwargs):

        array = []
        args = dict(kwargs)

        if 'exclude' in args: args['exclude'].append('../')

        args.setdefault('exclude', ['../'])
        args.setdefault('add_base', True)
        args.setdefault('recurse', False)

        if 'disk.yandex.ru' in target:
            url = 'https://getfile.dokpub.com/yandex/get/' + target
            logging.debug(f"{color('+', 'green')} {url}")
            return url

        if 'sourceforge.net' in target and not target.endswith('.iso'):
            sourceforge_array = []
            rss = rq.get(target.replace('/files/', '/rss?path=/')).text
            xml = xml_to_dict(rss)['rss']['channel']['item']
            if type(xml) is list:
                for entry in xml:
                    url = entry['media:content']['@url'][:-9]
                    if not url.endswith('.iso'): continue
                    size = int(entry['media:content']['@filesize'])
                    sourceforge_array.append({'url': url, 'size': size})
            elif type(xml) is dict:
                entry = xml['media:content']
                url = entry['@url'][:-9]
                size = int(entry['@filesize'])
                sourceforge_array.append({'url': url, 'size': size})
            else:
                logging.error("something wrong with sourceforge.net parser", exc_info=True)
            
            for url in sourceforge_array: logging.debug(f"{color('+', 'green')} {url}")

            return sourceforge_array

        def scrape(target, **kwargs):

            response = rq.get(target)
            pattern_html = re.compile(r'href=[\'|\"](.*?)[\'|\"]', re.S)
            urls = re.findall(pattern_html, str(response.text))

            for url in urls:
                if url in target: continue
                else:
                    if args['add_base']:
                        if not url.startswith('http'):
                            url = target + url
                    if any(x in url for x in args['exclude']):
                        continue
                    if 'pattern' in args:
                        pattern = re.compile(args['pattern'])
                        if not re.search(pattern, url):
                            continue

                if args['recurse'] and url.endswith('/'):
                    scrape(url, **args)
                if not '.iso' in url: continue
                if url.endswith('.iso/download'):
                    url = url[:-9]
                if url.endswith('.iso'):
                    url = str(unescape(url.replace('/./', '/')))
                    if url in target: continue
                    array.append(url)

        scrape(target, **args)

        result = list(dict.fromkeys(array))

        for url in result: logging.debug(f"{color('+', 'green')} {url}")

        return result


def copy_distro_logo(distro_id):
    """Copy specific logo.png to distro folder."""
    logo_src = f'{distros_dir}/{distro_id}/logo.png'
    logo_dst = f'{output_dir}/logos/{distro_id}.png'
    if not os.path.exists(logo_src):
        logos_dir = f'{working_dir}/website/logos'
        logo_src = f'{logos_dir}/{choice(os.listdir(logos_dir))}'
    copy(logo_src, logo_dst)


def get_distro_info(distro_id):
    """Parse specific info.json then return [distro_name, distro_url]."""
    target_json = f'{distros_dir}/{distro_id}/info.json'
    with open(target_json, 'r') as file:
        try:
            target_json = json.load(file)
            distro_info = (target_json['name'], target_json['url'])
        except:
            distro_url = f'https://google.com/search?q={distro_id}'
            distro_info = [distro_id, distro_url]
    return distro_info


def build_repo_entry(distro_id, distro_info):
    """Create a tulpe with distro values then return it."""

    target_file = f"{distros_dir}/{distro_id}/scraper.py"

    scraper = SourceFileLoader("scraper", target_file).load_module()

    repo_entry = {}
    repo_entry_releases = []

    repo_entry["id"] = distro_id
    repo_entry["name"] = distro_info[0]
    repo_entry["url"] = distro_info[1]

    tries = 3
    wait = 10

    for i in range(tries):
        try:
            distro_values = sorted(scraper.init(),
                                   key=lambda x: x[3],
                                   reverse=True)
        except requests.exceptions.RequestException as error:
            if i < tries - 1: # i is zero indexed
                logging.error(f"{distro_id}: {str(error).lower()}, retrying in {wait}s")
                sleep(wait)
                continue
            else:
                raise
        break



    for distro_value in distro_values:
        iso_url, iso_arch, iso_size, iso_version = distro_value
        a =  {"size": iso_size,
              "url": iso_url,
              "version": iso_version}
        if iso_arch is not None: a['arch'] = iso_arch
        repo_entry_releases.append(dict(sorted(a.items())))


    repo_entry["releases"] = repo_entry_releases

    if not repo_entry_releases:
        raise Exception('releases is empty')

    return repo_entry


def build_repo_html():

    markdown_distros = []

    markdown_distros_done = [x for x in distros_list if (x not in distros_errors)]
    markdown_distros_error = [x for x in distros_errors]

    with open(f"{output_dir}/repo.json", "r") as file:
        repo_json = file.read()

    with open(f"{working_dir}/website/body.md", "r") as file:
        markdown_source = file.read()

    with open(f"{output_dir}/list.txt", "w") as file:
        for distro_id in markdown_distros_done:
            distro_info = get_distro_info(distro_id)
            file.write(f"{distro_info[0]} ({distro_info[1]})\n")
            markdown_distros.append(f'<a href="{distro_info[1]}"><img title="{distro_info[0]}" class="distro_logo" src="./logos/{distro_id}.png"/></a>')

    markdown_distro_count = f'contains [{len(markdown_distros_done)}](./list.txt)'

    if markdown_distros_error:
        with open(f"{output_dir}/missing.txt", "w") as file:
            for distro_id in markdown_distros_error:
                distro_info = get_distro_info(distro_id)
                file.write(f"{distro_info[0]} ({distro_info[1]})\n")
        markdown_distro_count += f' and missing [{len(markdown_distros_error)}](./missing.txt)'

    markdown_formatted = markdown_source.format(
        count=markdown_distro_count,
        time=strftime('%Y.%m.%d %H:%M:%S'),
        timezone=strftime('%z')[:-2],
        distros="\n".join(markdown_distros))

    markdown_converted = markdown(markdown_formatted)

    with open(f"{working_dir}/website/template.html", "r") as file:
        html_template = file.read()

    with open(f"{output_dir}/index.html", "w") as file:
        file.write(html_template.format(body=markdown_converted))

        html_assets_dir = f'{working_dir}/website/root/'
        copytree(html_assets_dir, output_dir, dirs_exist_ok=True)


logo = color(f"""\
         __     _                __           _     __
    ____/ /____(_)   _____  ____/ /________  (_)___/ /
   / __  / ___/ / | / / _ \/ __  / ___/ __ \/ / __  /
  / /_/ / /  / /| |/ /  __/ /_/ / /  / /_/ / / /_/ /
  \__,_/_/  /_/ |___/\___/\__,_/_/ __\____/_/\__,_/
     ________  ____  ____  _____(_) /_____  _______  __
    / ___/ _ \/ __ \/ __ \/ ___/ / __/ __ \/ ___/ / / /
   / /  /  __/ /_/ / /_/ (__  ) / /_/ /_/ / /  / /_/ /
  /_/   \___/ .___/\____/____/_/\__/\____/_/   \__, /
           /_/                                /____/
""", 'white', attrs=['bold'])

if __name__ == "__main__":

    print(logo)

    filler = lambda: f"drivedroid://{random_hex(64)}/┗  "

    repo.append({
        "id": "repository",
        "name": "+ Repo",
        "url": "https://github.com/flameshikari/ddrg",
        "releases": [
            {
                "size": 1,
                "url": filler(),
                "version": "Last Update"
            },
            {
                "size": 2,
                "url": filler(),
                "version": "Distro Count"
            },
            {
                "size": 3,
                "url": filler(),
                "version": "Build Time"
            }
        ]
    })

    try:
        logging.info("started scraping distros")
        for distro_id in distros_list:
            try:
                distro_info = get_distro_info(distro_id)

                # check if scraper.py exists in specific
                # distro folder, else skip current iteration
                if os.path.isfile(f"{distros_dir}/{distro_id}/scraper.py"):
                    repo_entry = build_repo_entry(distro_id, distro_info)
                    repo.append(repo_entry)
                    logging.info(f"{color(distro_id, 'white', attrs=['underline'])} scraped")
                else:
                    raise Exception("missing scraper.py")

            except Exception as error:
                distros_errors.append(distro_id)
                logging.exception((f"[{distro_id}] {str(error).lower()}"))
                continue

        timer_stop = round(timer() - timer_start)
        build_time = strftime('%H:%M:%S', gmtime(timer_stop))

        if len(distros_errors) == len(distros_list):
            logging.critical("the repository isn't built, check scrapers", exc_info=True)
            exit(2)

        # remove previous output folder structure
        if os.path.exists(f"{output_dir}/repo.json"):
            rmtree(output_dir)

        # create output folder structure
        os.makedirs(f"{output_dir}/logos", exist_ok=True)

        # create repo.json in output folder
        with open(f"{output_dir}/repo.json", "w") as repo_json:
            repo[0]['releases'][0]['url'] += f"{strftime('%Y.%m.%d %H:%M:%S')} {strftime('%z')[:-2]}"
            repo[0]['releases'][1]['url'] += f"Contains: {len([x for x in distros_list if (x not in distros_errors)])} | Missing: {len([x for x in distros_errors])}"
            repo[0]['releases'][2]['url'] += f"{build_time}"
            json.dump(repo, repo_json, indent=2)

        # copy distro logos to distro folders
        for distro_id in distros_list:
            copy_distro_logo(distro_id)

        if options.generate:
            build_repo_html()

        logging.info(f"the repository is built, build time: {build_time}")

        if distros_errors:
            logging.warning(f"not included: {', '.join(distros_errors)}")

        exit(0)

    except KeyboardInterrupt:
        exit(130)

    except Exception as error:
        logging.critical(str(error).lower(), exc_info=True)
        exit(2)


__all__ = ["json", "re", "rq", "requests", "check_version", "get"]
