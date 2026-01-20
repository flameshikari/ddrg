from shared import *

info = ns(
    name='Memtest86+',
    url='https://memtest.org',
)

@scraper
def init():
    values = []

    regexp = r'_(\d+\.\d+)_'
    
    target = 'stash:memtest86plus'

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