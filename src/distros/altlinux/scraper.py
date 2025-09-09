from shared import *

info = ns(
    name='ALT Linux',
    url='https://altlinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)-'
    
    target = [
        'https://getalt.org/en/alt-workstation/',
        'https://getalt.org/en/alt-kworkstation/',
        'https://getalt.org/en/alt-server/',
        'https://getalt.org/en/alt-server-v/',
        'https://getalt.org/en/alt-education/',
        'https://getalt.org/en/simply/',
        'https://getalt.org/en/alt-workstation/'
    ]

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