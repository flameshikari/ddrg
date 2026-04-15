from shared import *

info = ns(
    name='Kaspersky Rescue Disk',
    url='https://kaspersky.com/downloads/free-rescue-disk',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+)/krd.iso'

    target = 'https://rescuedisk.s.kaspersky-labs.com/updatable/'
    
    for url, size in get.urls(target, recursive=True, exclude=['bases/']):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
