from shared import *

info = ns(
    name='TrueNAS',
    url='https://truenas.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(-\d+\.\d+)?)'
    
    target = [
        'https://www.truenas.com/download-truenas-core/',
        'https://www.truenas.com/download-truenas-scale/'
    ]

    for url, size in get.urls(target):

        arch = 'amd64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values