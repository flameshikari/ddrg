from shared import *

info = ns(
    name='Netboot',
    url='https://netboot.xyz',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+\.\d+\.\d+)/'
    
    target = 'https://github.com/netbootxyz/netboot.xyz/releases/latest'

    archs = ['multiarch', 'arm64']

    for url, size in get.urls(target):

        arch = next((arch for arch in archs if arch in url), 'x86_64')
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values