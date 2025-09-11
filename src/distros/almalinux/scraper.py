from shared import *

info = ns(
    name='AlmaLinux',
    url='https://almalinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)-'
    
    target = [
        'https://mirror.yandex.ru/almalinux/8/isos/',
        'https://mirror.yandex.ru/almalinux/9/isos/'
    ]

    exclude = ['latest']

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