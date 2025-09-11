from shared import *

info = ns(
    name='Alpine Linux',
    url='https://alpinelinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)'
    
    target = 'https://mirror.yandex.ru/mirrors/alpine/latest-stable/releases/'

    exclude = ['netboot', '_rc']

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