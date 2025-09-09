from shared import *

info = ns(
    name='MX Linux',
    url='https://mxlinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+(\.\d+)?)?)'

    target = 'https://mirror.truenetwork.ru/mxlinux-cd/MX/'
    
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
