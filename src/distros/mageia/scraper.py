from shared import *

info = ns(
    name='Mageia',
    url='https://mageia.org',
)

@scraper
def init():
    values = []

    regexp = r'Mageia-(\d+(\.\d+)?)-'

    target = 'https://mirror.yandex.ru/mageia/iso/'

    exclude = ['torrents']
    
    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
