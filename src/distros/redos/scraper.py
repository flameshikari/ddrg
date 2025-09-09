from shared import *

info = ns(
    name='RED OS',
    url='https://redos.red-soft.ru',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'
    
    target = 'https://redos.red-soft.ru/product/downloads/'
    
    exclude = ['live']

    for url, size in get.urls(target, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values