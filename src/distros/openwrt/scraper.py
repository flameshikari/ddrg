from shared import *

info = ns(
    name='OpenWRT [bigbugcc]',
    url='https://github.com/bigbugcc/OpenWrts',
)

@scraper
def init():
    values = []

    regexp = r'/download/[^/]*?(\d{4}\.\d{2}\.\d{2}-\d{6}|\d{11,14})(?:-\d+)?/'
    
    target = 'github:bigbugcc/OpenWrts'

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