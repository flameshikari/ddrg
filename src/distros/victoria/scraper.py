from shared import *

info = ns(
    name='Victoria',
    url='https://hdd.by',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'_(\d+(\.\d+(\w+)?)?)_')
    
    target = 'yandex:victoria'

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