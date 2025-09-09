from shared import *

info = ns(
    name='mAid',
    url='https://maid.binbash.rocks',
)

@scraper
def init():
    values = []

    regexp = r'v(\d+.\d+)'

    target = 'https://sourceforge.net/projects/maid-linux/files/'
    
    exclude = ['BETA', 'FWUL']

    for url, size in get.urls(target, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
