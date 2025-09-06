import json, logging, re

from html import unescape
from secrets import token_hex as random_hex
from time import strftime, sleep
from re import search
from urllib.parse import urlparse, urljoin
from pathlib import Path as path

try:
    import yaml
    from requests import Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from fake_useragent import UserAgent
    from termcolor import colored as color
    from xmltodict import parse as xml_to_dict
except ImportError as error:
    print(f"{error}. Did you install packages from requirements.txt?")
    exit(1)


def re_search(pattern, string, flags=0):
    # pattern = re.compile(pattern)
    result = search(pattern, string, flags)
    if result is None:
        raise ValueError(f"regexp failed at {color(string, 'cyan')}")
    return result

# re.search = re_search

def generate_status_entry(distros, errors, time):
    filler = lambda: f'drivedroid://{random_hex(64)}/┗  '
    last_update = f'{strftime('%Y.%m.%d %H:%M:%S')} {strftime('%z')[:-2]}'
    distro_count = f'Contains: {len([x for x in distros if (x not in errors)])} | Missing: {len([x for x in errors])}'
    build_time = time
    return {
        'id': 'repository',
        'name': '+ Repo',
        'url': 'https://dd.hexed.pw',
        'releases': [
            {
                'size': 1,
                'url': filler() + last_update,
                'version': 'Last Update'
            },
            {
                'size': 2,
                'url': filler() + distro_count,
                'version': 'Distro Count'
            },
            {
                'size': 3,
                'url': filler() + build_time,
                'version': 'Build Time'
            }
        ]
    }


def configure_requests():
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
    rq = Session()

    rq.headers.update({
        'User-Agent': str(UserAgent().firefox)
    })

    rq.mount('http://',  TimeoutHTTPAdapter(max_retries=retries))
    rq.mount('https://', TimeoutHTTPAdapter(max_retries=retries))

    return rq

rq = configure_requests()

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



def json_urls(target, pattern = '.*'):
    urls = []
    data = rq.get(target).json()
    pattern = re.compile(pattern)
    parsed = urlparse(target)
    def find(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                find(v)
        elif isinstance(obj, list):
            for item in obj:
                find(item)
        elif isinstance(obj, str):
            if obj.endswith('.iso'):
                if re.search(pattern, obj):
                    if not obj.startswith('http'):
                        obj = urljoin(f'http://{parsed.netloc}', obj)
                    urls.append(obj)
    find(data)
    return urls

def github_urls(url):
    response = rq.head(url).headers
    if 'Location' in response:
        url = response['Location']
    pattern = r'https://github\.com/([^/]+/[^/]+)/releases/tag/([^/]+)'
    match = re.match(pattern, url)
    if not match:
        return "Error: URL format is incorrect"
    repo, tag = match.groups()
    api_url = f"https://api.github.com/repos/{repo}/releases/tags/{tag}"
    response = rq.get(api_url)
    if response.status_code != 200:
        return f"Error: Release tag '{tag}' not found or API error."
    release_data = response.json()
    iso_assets = [asset['browser_download_url'] for asset in release_data.get('assets', [])
                  if asset['name'].endswith('.iso') or asset['name'].endswith('.img')]
    return iso_assets


class get:

    def arch(target):

        target = path(target).name

        if 'powerpc' in target:
            target = target.replace('powerpc', 'ppc')

        for key, value in archs.items():
            for arch in value:
                if arch in target:
                    return arch if key == 'all' else key

        return None

    def size(target):
        try:
            if (type(target) == int):
                size = target
            else:
                sleep(0.05)
                headers = rq.head(target, allow_redirects=True).headers
                size = int(headers['Content-Length'])
            prefix = color('0'*(11 - len(str(size))), 'dark_grey') + color(str(size), 'blue')
            logging.debug(f"{color('+', 'green')} {prefix} {color(target, 'dark_grey')}")
            return size
        except Exception as error:
            prefix = color('0'*11, 'dark_grey')
            logging.debug(f"{color('-', 'red')} {prefix} {color(target, 'dark_grey')} {color(str(error).lower(), 'red')}")
            pass

    def urls(target, **kwargs):

        args = dict(kwargs)

        args.setdefault('exclude', ['../', 'magnet:'])
        args.setdefault('add_base', True)
        args.setdefault('recursive', False)
        args.setdefault('json', False)
        args.setdefault('pattern', '.*')

        if 'exclude' in args: args['exclude'].append('../')

        if target.endswith('.json') or args['json']:
            return json_urls(target, args['pattern'])

        if 'github.com' in target:
            return github_urls(target)

        if 'disk.yandex.ru' in target:
            return target.replace('yandex.ru', 'hexed.pw')

        if 'sourceforge.net' in target:
            if not target.endswith('.iso'):
                sourceforge_array = []
                rss = rq.get(target.replace('/files/', '/rss?path=/')).text
                xml = xml_to_dict(rss)['rss']['channel']['item']
                if type(xml) is list:
                    for entry in xml:
                        url = entry['media:content']['@url'][:-9]
                        if not url.endswith('.iso'): continue
                        size = int(entry['media:content']['@filesize'])
                        if not any(x in url for x in args['exclude']):
                            sourceforge_array.append({'url': url, 'size': size})
                            prefix = color('0'*(11 - len(str(size))), 'dark_grey') + color(str(size), 'blue')
                            logging.debug(f"{color('+', 'green')} {prefix} {color(url, 'dark_grey')}")
                elif type(xml) is dict:
                    entry = xml['media:content']
                    url = entry['@url'][:-9]
                    size = int(entry['@filesize'])
                    if not any(x in url for x in args['exclude']):
                        sourceforge_array.append({'url': url, 'size': size})
                        prefix = color('0'*(11 - len(str(size))), 'dark_grey') + color(str(size), 'blue')
                        logging.debug(f"{color('+', 'green')} {prefix} {color(url, 'dark_grey')}")
                else:
                    logging.error("something wrong with sourceforge.net parser", exc_info=True)

                return sourceforge_array

        if target.endswith('.iso'):
            return target

        array = []

        def scrape(target, **kwargs):
            response = rq.get(target)
            pattern_html = re.compile(r'href=["\']?\n?((?:.(?!["\']?\s+(?:\S+)=|\s*\/?[>"\']))+.\/?)\n?["\']?', re.S)
            urls = re.findall(pattern_html, str(response.text))

            extensions = ['.iso', '.ISO', '.img', '.IMG']

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
                        try:
                            re.search(pattern, url)
                        except:
                            continue

                if url.startswith('//'):
                    url = 'http:' + url

                if args['recursive'] and url.endswith('/'):
                    scrape(url, **args)

                if not any(ext in url for ext in extensions): continue
                if any(url.endswith(ext + '/download') for ext in extensions):
                    url = url[:-9]
                if any(url.endswith(ext) for ext in extensions):
                    url = str(unescape(url.replace('/./', '/')))
                    if url in target: continue
                    # logging.debug(f"{color('+', 'green')} {url}")
                    array.append(url)

        scrape(target, **args)

        result = list(dict.fromkeys(array))

        return result


__all__ = [
    'get',
    'json',
    're',
    'rq',
    'color',
    'logging',
    'yaml'
]