from shared import *

info = ns(
    name='iPXE',
    url='https://ipxe.org',
)

@scraper
def init():
    values = []

    versions = rq.get('https://api.github.com/repos/ipxe/ipxe/tags').json()
    
    target = 'https://boot.ipxe.org/ipxe.iso'

    for url, size in get.urls(target):

        arch = get.arch(url)
        version = versions[0]['name'][1:]

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values