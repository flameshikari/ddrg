from shared import *

info = ns(
    name='Arch Linux',
    url='https://archlinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'

    target = 'https://mirror.yandex.ru/archlinux/iso/'
    
    exclude = ['archlinux-x86_64', 'arch/', 'latest/']

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
