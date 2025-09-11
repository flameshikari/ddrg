from shared import *

info = ns(
    name='grml',
    url='https://grml.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d{4}.\d{2}(.\d{2})?)'

    target = 'https://grml.org/download'
    
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
