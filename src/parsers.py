from html import unescape
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from public import *  # noqa
import threading
from signal import signal, SIGINT
import traceback
def signal_handler(sig, frame): exit(130)
signal(SIGINT, signal_handler)


class get:

    def size(target):
        """Returns the file size of the target URL in bytes."""
        if target.startswith("http"):
            size = int(rq.get(target, stream=True).headers['Content-Length'])
            if size < 500: raise Exception('very low size, probably wrong URL')
            return size
        else:
            return 0

    def arch(target):
        """Returns the used processor architecture of the target URL."""

        archs_all = [
            "i386", "amd64",
            "arm64", "arm32", "armhfp", "armhf", "armv7", "armel", "aarch64",
            "i486", "i586", "i686-pae", "i686", "ia64",
            "ppc64le", "ppc64el", "ppc64", "ppcspe", "ppc",
            "mips64el", "mipsel", "mips",
            "s390x", "hppa", "macppc", "alpha", "sparc64",
            "bios", "efi", "ipxe"
        ]

        archs_86_64 = ["86_64", "86-64", "96", "archboot"]
        archs_64 = ["x64", "64bit", "dual", "64"]
        archs_86 = ["x86", "x32", "32bit", "386", "32"]

        for arch in archs_all:
            if arch in target:
                return arch

        if any(arch in target for arch in archs_86_64):
            return "x86_64"

        elif "powerpc" in target:
            for ppc in archs_all:
                if ppc in target.replace("powerpc", "ppc"):
                    return ppc

        elif any(arch in target for arch in archs_64):
            return "amd64"

        elif any(arch in target for arch in archs_86):
            return "i386"

        elif "legacy" in target:
            return "bios"

        else:
            return "unk"


    def urls(target, **kwargs):

        array = []
        args = dict(kwargs)

        if 'exclude' in args: args['exclude'].append('../')

        args.setdefault('exclude', ['../'])
        args.setdefault('add_base', True)
        args.setdefault('recurse', False)

        if 'disk.yandex.ru' in target:
            return 'https://getfile.dokpub.com/yandex/get/' + target

        def scrape(target, **kwargs):

            headers = {'User-Agent': user_agent().random}
            response = rq.get(target, headers=headers)
            pattern_html = re.compile(r'href=[\'|\"](.*?)[\'|\"]', re.S)
            urls = re.findall(pattern_html, str(response.text))

            for url in urls:
                if url in target:
                    continue
                if 'sourceforge.net' in target:
                    pattern = re.compile('/projects/.*/files')
                    if not re.findall(pattern, url):
                        continue
                    if url.startswith('/'):
                        url = 'https://sourceforge.net' + url
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
                    array.append(url)
                    logger(f'[+] {url}')

        scrape(target, **args)

        return array
