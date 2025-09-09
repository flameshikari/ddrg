from shared import *

info = ns(
    name='AdminPE',
    url='https://adminpe.ru',
)

@scraper
def init():
    values = []

    regexp = r'_(\d+(\.\d+)?)_'
    
    target = 'yandex:adminpe'

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