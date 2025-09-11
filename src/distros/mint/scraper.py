from shared import *

info = ns(
    name='Linux Mint',
    url='https://linuxmint.com',
)

@scraper
def init():
    values = []

    regexp = r'l\w+-(\d+(\.\d+)?)-'

    target = 'https://mirror.yandex.ru/linuxmint/'
    
    for url, size in get.urls(target, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
