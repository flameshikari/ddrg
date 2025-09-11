from shared import *

info = ns(
    name='DragonFlyBSD',
    url='https://dragonflybsd.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+\.\d+)'

    target = 'https://mirror.macomnet.net/pub/DragonFlyBSD/iso-images/'
    
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
