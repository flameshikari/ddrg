from shared import *

info = ns(
    name='BunsenLabs',
    url='https://www.bunsenlabs.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(.\d+)?)'

    target = 'https://ddl.bunsenlabs.org/ddl/'
    
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
