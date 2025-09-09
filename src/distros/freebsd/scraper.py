from shared import *

info = ns(
    name='FreeBSD',
    url='https://freebsd.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)'

    target = 'https://mirror.yandex.ru/freebsd/releases/ISO-IMAGES/'
    
    exclude = ['-RC']

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
