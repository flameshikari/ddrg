from shared import *

info = ns(
    name='MemTest86',
    url='https://memtest86.com',
)

@scraper
def init():
    values = []

    regexp = r'_(\d+\.\d+(\.\d+)?)_'
    
    target = 'stash:memtest86'

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