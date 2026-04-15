from shared import *

info = ns(
    name='Ubuntu',
    url='https://ubuntu.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)-'
    
    target = 'https://mirror.yandex.ru/ubuntu-releases/'

    pattern = r'\/\d+\.\d+(.\d+)?\/'

    for url, size in get.urls(target, recursive=True, pattern=pattern, exclude=['/releases/']):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values