from shared import *

info = ns(
    name='Vanilla OS',
    url='https://vanillaos.org',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'\.(\d+)\.')
    
    target = 'stash:vanilla'

    for url, size in get.urls(target, recursive=False):

        arch = 'amd64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values