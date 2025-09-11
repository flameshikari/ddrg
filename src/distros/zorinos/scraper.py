from shared import *

info = ns(
    name='Zorin OS',
    url='https://zorinos.com',
)

@scraper
def init():
    values = []

    regexp = r'Zorin-OS-((\d+)\.?\d+)-'
   
    target = 'https://mirrors.edge.kernel.org/zorinos-isos/'

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