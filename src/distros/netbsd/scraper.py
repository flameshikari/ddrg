from shared import *

info = ns(
    name='NetBSD',
    url='https://netbsd.org',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+\.\d+)/'

    target = 'https://mirror.yandex.ru/NetBSD/iso/'

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