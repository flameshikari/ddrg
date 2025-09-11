from shared import *

info = ns(
    name='GParted',
    url='https://gparted.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+\.\d+-\d+)'

    target = 'https://sourceforge.net/projects/gparted/files/gparted-live-stable/'
    
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
