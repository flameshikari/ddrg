from shared import *

info = ns(
    name='IPFire',
    url='https://ipfire.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+)-'

    target = 'https://www.ipfire.org/download'
    
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
