from shared import *

info = ns(
    name='BackBox',
    url='https://backbox.org',
)

@scraper
def init():
    values = []

    regexp = r'backbox-(\d+)'

    target = 'https://backbox.mirror.garr.it/'

    for url, size in get.urls(target):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
