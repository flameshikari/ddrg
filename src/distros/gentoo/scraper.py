from shared import *

info = ns(
    name='Gentoo',
    url='https://gentoo.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)T'

    target = 'https://www.gentoo.org/downloads/'
    
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
