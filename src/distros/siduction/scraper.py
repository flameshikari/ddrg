from shared import *

info = ns(
    name='siduction',
    url='https://siduction.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(.\d+)?)'

    target = 'https://ftp.spline.de/pub/siduction/iso/'
    
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