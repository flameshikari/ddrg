from shared import *

info = ns(
    name='CachyOS',
    url='https://cachyos.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)'

    target = 'https://mirror.cachyos.org/ISO/'
    
    for url, size in get.urls(target, recursive=True):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
