from shared import *

info = ns(
    name='Tiny Core Linux',
    url='https://mirrors.dotsrc.org/tinycorelinux',
)


def get_version():
    target = 'http://tinycorelinux.net/downloads.html'
    response = str(rq.get(target).text)
    regexp = re.compile(r'Version (\d+).\d+')
    return re.search(regexp, response).group(1)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+)\.'
    
    version_base = get_version()

    target = [
        f'http://tinycorelinux.net/{version_base}.x/x86/release/',
        f'http://tinycorelinux.net/{version_base}.x/x86_64/release/'
    ]

    exclude = ['current']

    for url, size in get.urls(target, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values