from shared import *

info = ns(
    name='Arch Linux 32',
    url='https://archlinux32.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+(\.\d+)?)?)'

    target = 'https://mirror.yandex.ru/archlinux32/archisos/'
    
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
