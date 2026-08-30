from shared import *

info = ns(
    name='KaOS',
    url='https://kaosx.us',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)-'

    target = 'https://mirror.math.princeton.edu/pub/kaoslinux/'
    
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
