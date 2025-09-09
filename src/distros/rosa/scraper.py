from shared import *

info = ns(
    name='ROSA',
    url='https://rosalinux.ru',
)

@scraper
def init():
    values = []

    regexp = r'\.(\d+(\.\d+(\.\d+)?)?)?\.\w+'
    
    target = 'https://rosa.ru/rosa-linux-download-links/'

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