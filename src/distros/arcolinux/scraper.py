from shared import *

info = ns(
    name='ArcoLinux',
    url='https://arcolinux.com',
)

@scraper
def init():
    values = []

    regexp = r'(\d+\.\d+\.\d+)'

    target = 'https://sourceforge.net/projects/arconetpro/files/'
    
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
