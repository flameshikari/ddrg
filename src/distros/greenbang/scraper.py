from shared import *

info = ns(
    name='GreenBANG',
    url='https://archbang.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)'

    target = 'https://sourceforge.net/projects/archbang/files/'
    
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
