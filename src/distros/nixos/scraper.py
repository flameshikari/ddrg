from shared import *

info = ns(
    name='NixOS',
    url='https://nixos.org',
)

@scraper
def init():
    values = []

    regexp = r'nixos-(\d+\.\d+)/'

    target = 'https://nixos.org/download.html'
    
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
