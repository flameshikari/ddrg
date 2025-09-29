import json, logging, re

from html import unescape
from secrets import token_hex as random_hex
from time import gmtime, strftime, sleep
from re import search
from urllib.parse import urlparse, urljoin
from pathlib import Path as path
from shutil import copytree
from copy import deepcopy
from sys import exit

from datetime import datetime

from importlib.machinery import SourceFileLoader

from os import listdir
from os.path import exists, join

from itertools import chain

from config import config
from log import log

try:
    import yaml
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from requests.exceptions import RequestException
    from fake_useragent import UserAgent
    from termcolor import colored as color
    from natsort import natsorted
    from xmltodict import parse as xml_to_dict
    from markdown2 import markdown

    from bs4 import BeautifulSoup as bs
except ImportError as error:
    print(f"{error}. Did you install packages from requirements.txt?")
    exit(1)


archs = {
    # https://wiki.netbsd.org/ports/
    'all': [
        'x86_64', 'amd64', 'i386', 'arm64',
        'ia64', 'i686', 'i586', 'i486',
        'power9', 's390x', 's390', 'e2k', 'vax',
        'riscv64', 'riscv',
        'hppa', 'sparc64', 'sparc', 'alpha',
        'ipxe', 'bios', 'uefi',
    ],
    'arm64': ['aarch64'],
    'arm': [
        'armhfp', 'armhf', 'armel', 'arm32', 'aarch32', 'armv7', 'armv6',
        'armv5', 'acorn32', 'cats', 'epoc32', 'evbarm', 'hpcarm',
        'iyonix', 'netwinder', 'shark', 'zaurus',
    ],
    'mips': [
        'emips', 'evbmips', 'ews4800mips', 'mipsco',
        'newsmips', 'sbmips', 'sgimips', 'algor', 'arc',
        'cobalt', 'hpcmips', 'pmax', 'sbmips',
    ],
    'ppc': [
        'amigappc', 'bebox', 'evbppc', 'ibmnws', 'macppc',
        'mvmeppc', 'ofppc', 'prep', 'rs6000', 'sandpoint',
        'ppc64le', 'ppc64el', 'ppc64', 'ppcspe',
    ],
    'sh3': [
        'evbsh3', 'mmeye', 'dreamcast', 'evbsh3', 'landisk', 'hpcsh',
    ],
    'm68k': [
        'amiga', 'atari', 'cesfic', 'hp300', 'luna68k', 'mac68k',
        'mvme68k', 'news68k', 'next68k', 'sun3', 'sun2', 'x68k'
    ],
    'loong64': ['loongarch64', 'loongson'],
    'x86_64': ['86_64', '86-64', '96', 'xen'],
    'amd64': ['x64', '64-bit', '64bit', 'dual'],
    'i386': ['x86', 'x32', '32-bit', '32bit', '386'],
    'bios': ['legacy'],
    'uefi': ['efi'],
}

exts = ['.iso', '.img', '.ISO', '.IMG']

def requests_wrapper():
    # https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
    DEFAULT_TIMEOUT = 5 # seconds
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

    retries = Retry(total=10, status_forcelist=[429, 500, 502, 503, 504])
    rq = Session()

    rq.headers.update({
        'User-Agent': str(UserAgent().firefox)
    })

    rq.mount('http://',  TimeoutHTTPAdapter(max_retries=retries))
    rq.mount('https://', TimeoutHTTPAdapter(max_retries=retries))

    return rq

rq = requests_wrapper()


def list_distros(local = True):
    distros = listdir(config.paths.input)
    if config.args.distros and not config.args.list:
        distros = list(chain.from_iterable(config.args.distros))
    if config.args.exclude:
        exclude = list(chain.from_iterable(config.args.exclude))
        distros = [x for x in distros if x not in exclude]
    distros = sorted([distro for distro in distros if not distro.startswith('_')])
    return distros

if config.args.list:
    distros_list = list_distros()
    if len(distros_list) == 0:
        exit(1)
    else:
        print('\n'.join(distros_list))
        exit(0)


def load_distros(distros):
    modules = {}

    for distro in distros:
        target_dir = f'{config.paths.input}/{distro}'

        if not path(target_dir).is_dir():
            log.custom.sys(f'distro {color(distro, 'cyan')} does not exists', 'warning')
            continue
        else:
            if not exists(f'{target_dir}/scraper.py'):
                log.custom.sys(f'{color(distro, 'cyan')} scraper not found', 'warning')
                continue

            if not exists(f'{target_dir}/logo.png'):
                log.custom.sys(f'{color(distro, 'cyan')} logo not found', 'warning')
                continue

        try:
            modules[distro] = SourceFileLoader(distro, f'{target_dir}/scraper.py').load_module()

        except Exception as error:
            log.error(f"{color(distro, 'yellow', attrs=['underline'])}: {error}")
            continue

    return modules


def find_by_id(json_array, target_id):
    filtered = list(filter(lambda item: item.get('id') == target_id, json_array))
    return filtered[0] if filtered else None


def scraper(func):
    def wrapper():
        values = []
        try:
            values = func()
        except KeyboardInterrupt:
            exit(130)
        except Exception as error:
            raise Exception(error)
        return values
    return wrapper

class parser:

    def url(target, args):
        url = target
        size = get.size(url)
        if size:
            log.custom.url(url, size)
            return [(url, size)]
    
    def json(target, args):
        array = []
        data = rq.get(target).json()
        pattern = re.compile(args['pattern'])
        parsed = urlparse(target)
        def find(url):
            if isinstance(url, dict):
                for k, v in url.items():
                    find(v)
            elif isinstance(url, list):
                for item in url:
                    find(item)
            elif isinstance(url, str):
                if any(url.endswith(ext) for ext in exts):
                    if re.search(pattern, url):
                        if not url.startswith('http'):
                            url = urljoin(f'http://{parsed.netloc}', url)
                        size = get.size(url)
                        if size:
                            array.append((url, size))
                            log.custom.url(url, size)

        find(data)
        return array

    def github(target, args):
        values = []
        response = rq.head(target).headers
        if 'Location' in response:
            target = response['Location']
        pattern = r'https://github\.com/([^/]+/[^/]+)/releases/tag/([^/]+)'
        match = re.match(pattern, target)
        if not match:
            return "Error: URL format is incorrect"
        repo, tag = match.groups()
        api_url = f"https://api.github.com/repos/{repo}/releases/tags/{tag}"
        response = rq.get(api_url)
        if response.status_code != 200:
            return f"Error: Release tag '{tag}' not found or API error."
        assets = response.json()['assets']
        
        for asset in assets:
            name = asset['name']
            size = asset['size']
            url = asset['browser_download_url']
            if any(name.endswith(ext) for ext in exts):
                values.append((url, size))
                log.custom.url(url, size)
        
        return values

    def sourceforge(target, args):

        if any(target.endswith(ext) for ext in exts): return

        values = []

        def scrape(path = '', limit = 5000):
            rss = rq.get(target.replace('/files/', f'/rss?limit={limit}&path=/') + path).text            
            try:
                xml = xml_to_dict(rss)['rss']['channel']['item']
            except:
                return
            if type(xml) is list:
                for entry in xml:
                    url = entry['media:content']['@url'][:-9]
                    if not any(url.endswith(ext) for ext in exts): continue
                    size = int(entry['media:content']['@filesize'])
                    if not any(x in url.replace('files/', '') for x in args['exclude']):
                        values.append((url, size))
                        log.custom.url(url, size)
            elif type(xml) is dict:
                entry = xml['media:content']
                url = entry['@url'][:-9]
                size = int(entry['@filesize'])
                if not any(x in url for x in args['exclude']):
                    values.append((url, size))
                    log.custom.url(url, size)

        if args['recursive']:
            response = rq.get(target)
            soup = bs(response.text, 'html.parser')
            trs = soup.find_all('tr', class_='folder')

            titles = []
            for tr in trs:
                try:
                    tr = tr.get('title')
                    if not any(x in tr for x in args['exclude']):
                        titles.append(tr)
                except:
                    continue

            for title in titles:
                scrape(title)

        else:
            scrape()
        
        return values

    def yandex(target, args):
        shared = 'YHflGF3zn3vf3w'

        if target.startswith('yandex:'):
            id = target.split(':')[1]
            target = f'https://disk.hexed.pw/list/d/{shared}/{id}'
        else:
            return target.replace('//disk.yandex.ru/', '//disk.hexed.pw/')

        files = rq.get(target).json()

        values = []

        for file in files:
            name = file['name']
            size = file['size']

            if any(name.endswith(ext) for ext in exts):
                url = join(target.replace('/list/', '/'), name)
                values.append((url, size))
                log.custom.url(url, size)

        return values
    
    def common(target, args):
        array = []
        def scrape(target, **kwargs):
            try:
                response = rq.get(target)
            except:
                response = rq.get(target, verify=False)
            soup = bs(str(response.text), 'html.parser')
            urls = [a['href'] for a in soup.find_all('a', href=True)]

            # pattern_html = re.compile(r'href=["\']?\n?((?:.(?!["\']?\s+(?:\S+)=|\s*\/?[>"\']))*?\/?)\n?["\']?', re.S)
            # urls = re.findall(pattern_html, str(response.text))

            for url in urls:

                url = url.strip()

                if url.startswith('ftp://'): continue

                if url in target: continue
                else:

                    if args['rewrite']:
                        pattern = re.compile(args['rewrite'][0])
                        replace = args['rewrite'][1]
                        url = re.sub(pattern, replace, url)

                    if 'resolve_scheme' in args:
                        if url.startswith('//'):
                            url = urlparse(args['resolve_scheme']).scheme + ':' + url

                    if args['add_base'] == True:
                        if not url.startswith('http'):
                            url = target + url
                    else:
                        url = args['add_base'] + url

                    skip = False
                    
                    if any(x in url for x in args['exclude']):
                        skip = True
                    
                    if args['pattern'] != '.*':
                        pattern = re.compile(args['pattern'])
                        try:
                            re.search(pattern, url).group(0)
                        except:
                            skip = True

                    if skip: continue

                if not args['follow']:
                    if urlparse(target).hostname not in url:
                        continue

                if args['recursive'] and url.endswith('/'):
                    scrape(url, **args)

                if not any(ext in url for ext in exts):
                    continue
                
                if any(url.endswith(ext + '/download') for ext in exts):
                    url = url[:-9]
                
                if any(url.endswith(ext) for ext in exts):
                    url = str(unescape(url.replace('/./', '/')))
                    if url in target: continue

                    if args['filter']:
                        pattern = re.compile(args['filter'])
                        try:
                            re.search(pattern, url).group(0)
                        except:
                            continue

                    if all(x[0] != url for x in array):
                        size = get.size(url)
                        if size:
                            array.append((url, size))
                            log.custom.url(url, size)


        scrape(target, **args)

        return array

class get:

    def version(target, regexp):
        return re.search(regexp, target).group(1)

    def arch(target, fallback = None):
        target = path(target).name
        if 'powerpc' in target:
            target = target.replace('powerpc', 'ppc')
        for key, value in archs.items():
            for arch in value:
                if arch in target:
                    return arch if key == 'all' else key
        
        return fallback if fallback else None

    def size(target):
        try:
            if (type(target) == int):
                size = target
            else:
                sleep(0.25)
                response = rq.head(target, allow_redirects=True)
                status = response.status_code
                headers = response.headers
                if status != 200:
                    log.custom.url(target, status, False)
                    return None
                size = int(headers['Content-Length'])
            return size
        except RequestException as error:
            raise Exception('scraping failed ' + color('# ' + str(error), 'dark_grey'))
        except Exception:
            raise Exception(f'cannot get size for {color(path(target).name, 'blue')} {color('# ' + target, 'dark_grey')}')

    def urls(target, **kwargs):

        args = dict(kwargs)

        exclude = ['../', 'magnet:']

        args.setdefault('exclude', exclude)
        args.setdefault('add_base', True)
        args.setdefault('recursive', False)
        args.setdefault('json', False)
        args.setdefault('pattern', '.*')
        args.setdefault('rewrite', None)
        args.setdefault('follow', True)
        args.setdefault('fix_scheme', None)
        args.setdefault('filter', None)

        if 'exclude' in args:
            args['exclude'] = exclude + args['exclude']

        result = []

        if type(target) != list: target = [target]

        for entry in target:

            if entry.endswith('.json') or args['json']:
                selected = parser.json

            elif '//github.com/' in entry:
                selected = parser.github

            elif '//sourceforge.net/' in entry:
                selected = parser.sourceforge

            elif '//disk.yandex.ru/' in entry or entry.startswith('yandex:'):        
                selected = parser.yandex

            elif any(entry.endswith(ext) for ext in exts):
                selected = parser.url

            else:
                selected = parser.common

            values = selected(entry, args)

            result.append(values)

        result = list(chain.from_iterable(result))

        return result


class build:
    def meta(status):
        format = lambda text: f'dd{random_hex(100)}:/// >   {text}'
        distro_count = f'Included: {len(status.distros.included)}⧸{status.distros.total} | Outdated: {len(status.distros.outdated)}'
        last_update = datetime.fromisoformat(status.last_update).strftime('%Y.%m.%d %H:%M:%S %z')
        build_time = strftime('%H:%M:%S', gmtime(status.build_time))

        return {
            'id': 'repository',
            'name': '# Repository',
            'url': 'https://dd.hexed.pw',
            'status': {
                'build_time': status.build_time,
                'last_update': status.last_update,
                'distros': {
                    'total': status.distros.total,
                    'excluded': status.distros.excluded,
                    'outdated': status.distros.outdated,
                },
            },
            'releases': [
                {
                    'size': 1,
                    'url': format(distro_count),
                    'version': '•︎ Distro Count' 
                },
                {
                    'size': 2,
                    'url': format(last_update),
                    'version': '▸ Last Update'
                },
                {
                    'size': 3,
                    'url': format(build_time),
                    'version': '▪ Build Time'
                }
            ]
        }
    
    def entry(distro, releases = []):

        releases = deepcopy(releases)

        id, module = distro

        entry = {
            'id': id,
            'name': module.info.name,
            'url': module.info.url,
            'releases': releases,
        }

        if len(releases) > 0:
            return entry

        releases = natsorted(
            module.init(),
            key=lambda x: x.version,
            reverse=True,
        )

        for release in releases:
            
            values = {
                'size': release.size,
                'url': release.url,
                'version': release.version,
            }
            
            if release.arch != None:
                values['arch'] = release.arch
            
            values = dict(sorted(values.items()))

            entry['releases'].append(values)

        # if not entry['releases']:
        #     log(distro, 'releases is empty', 'error')
        #     return entry

        return entry


    def html(status):
        target = 'repo.json'

        content = {
            'included': {
                'distros': status.distros.included,
                'char': '■',
            },
            'outdated': {
                'distros': status.distros.outdated,
                'char': '▨',
            },
            'excluded': {
                'distros': status.distros.excluded,
                'char': '□',
            },
        }

        html = ''

        for key, value in content.items():
            distros = value['distros']
            if distros:
                html += f'<h3><span class="color">{value['char']}</span> {key.capitalize()}</h3>\n'
                p = ''
                for info in distros:
                    p += f'<a target="_blank" href="{info.url}"><img title="{info.name}" loading="lazy" class="distro_logo" src="./logos/{info.id}.png"/></a>\n'
                html += f'<p class="start">{p}</p>\n'



        markdown_distro_count = f'includes [{len(content['included']['distros'])}](/repo.json) of [{status.distros.total}](https://github.com/flameshikari/ddrg/tree/master/src/distros) distros'

        if content['outdated']['distros']:
            markdown_distro_count += f' with [{len(content['outdated']['distros'])}](/repo.json) outdated'

        with open(f"{config.paths.root}/website/body.md", "r") as file:
            markdown_source = file.read()

        date = datetime.fromisoformat(status.last_update).strftime('%Y.%m.%d %H:%M:%S %z')


        markdown_formatted = markdown_source.format(
            count=markdown_distro_count,
            time=date,
            timezone=strftime('%z')[:-2],
            content=html,
        )

        markdown_converted = markdown(markdown_formatted)

        with open(f"{config.paths.root}/website/index.html", "r") as file:
            html_template = file.read()

        # with open(f"{config.paths.output}/{target}", "w") as file:
        #     file.write(json.dumps(status, indent=2, default=lambda x: x.__dict__))

        with open(f"{config.paths.output}/index.html", "w") as file:
            file.write(html_template.format(body=markdown_converted))

        html_assets_dir = f'{config.paths.root}/website/root/'
        copytree(html_assets_dir, config.paths.output, dirs_exist_ok=True)
