from shared import *

info = ns(
    name='Super Grub2 Disk',
    url='https://www.supergrubdisk.org/',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+\.\d+)'

    target = 'https://sourceforge.net/projects/supergrub2/files/'
    
    exclude = [
        'tmp',
        'beta',
        '-rc',
    ]

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
