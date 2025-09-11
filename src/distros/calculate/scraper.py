from shared import *

info = ns(
    name='Calculate Linux',
    url='https://calculate-linux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)-x86_64'

    target = [
        'https://wiki.calculate-linux.org/desktop',
        'https://wiki.calculate-linux.org/server'
    ]
    
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
