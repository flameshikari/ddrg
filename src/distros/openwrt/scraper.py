from shared import *

info = ns(
    name='OpenWRT',
    url='https://openwrt.org',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+\.\d+\.\d+-\d+)/'
    
    target = 'https://github.com/bigbugcc/OpenWrts/releases/latest'

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