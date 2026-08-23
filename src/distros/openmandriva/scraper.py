from shared import *

info = ns(
    name='OpenMandriva',
    url='https://openmandriva.org',
)

@scraper
def init():
    values = []

    regexp = r'release_current\/(\d+\.\d+|\w+)\/'

    target = 'https://mirror.openmandriva.org/downloads'
    
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
