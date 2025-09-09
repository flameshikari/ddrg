from shared import *

info = ns(
    name='BlackArch Linux',
    url='https://blackarch.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+\.\d+)-'

    target = 'https://mirror.yandex.ru/mirrors/blackarch/iso/'
    
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
