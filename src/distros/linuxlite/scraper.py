from shared import *

info = ns(
    name='Linux Lite',
    url='https://linuxliteos.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)-'

    target = 'https://mirror.alpix.eu/linuxliteos/isos/'
    
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
