from shared import *

info = ns(
    name='Ophcrack',
    url='https://ophcrack.sourceforge.io',
)

@scraper
def init():
    values = []

    regexp = r'\/(\d+\.\d+(\.\d+)?)\w?\/'

    target = 'https://sourceforge.net/projects/ophcrack/files/ophcrack-livecd/'
    
    for url, size in get.urls(target):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
