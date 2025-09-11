from shared import *

info = ns(
    name='TempleOS',
    url='https://templeos.org',
)

@scraper
def init():
    values = []

    target = 'https://templeos.org/Downloads/'

    for url, size in get.urls(target):

        arch = 'amd64'
        version = '5.03'

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values