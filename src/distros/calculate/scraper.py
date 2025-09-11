from shared import *

info = ns(
    name='Calculate Linux',
    url='https://calculate-linux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)-x86_64'

    target = 'https://mirror.calculate-linux.org/release/'
    
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
