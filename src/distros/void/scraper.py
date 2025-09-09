from shared import *

info = ns(
    name='Void Linux',
    url='https://voidlinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d{8})'
    
    target = 'https://mirror.yandex.ru/mirrors/voidlinux/live/current/'

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