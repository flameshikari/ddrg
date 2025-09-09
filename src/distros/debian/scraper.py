from shared import *

info = ns(
    name='Debian',
    url='https://debian.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)'

    target = [
        'https://mirror.yandex.ru/debian-cd/current/',
        'https://mirror.yandex.ru/debian-cd/current-live/',
    ]
    
    exclude = [
        'bt-', 
        'jigdo-', 
        'list-',
        'log',
        'source',
        'trace',
        'log',
    ]

    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
