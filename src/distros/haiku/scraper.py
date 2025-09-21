from shared import *

info = ns(
    name='Haiku',
    url='https://www.haiku-os.org',
)

@scraper
def init():
    values = []

    regexp = r'\/(r\d+\w+\d+(\.\d+)?)\/'

    target = 'https://mirror.truenetwork.ru/haiku/release/'
    
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
