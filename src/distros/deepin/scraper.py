from shared import *

info = ns(
    name='Deepin',
    url='https://deepin.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+(\.\d+)?)?|-\w+)-'

    target = 'https://cdimage.deepin.com/releases/'
    
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
