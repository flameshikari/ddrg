from shared import *

info = ns(
    name='ChimeraOS',
    url='https://chimeraos.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)-'
    
    target = 'github:ChimeraOS/install-media?latest'    

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