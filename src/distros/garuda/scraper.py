from shared import *

info = ns(
    name='Garuda',
    url='https://garudalinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+).iso'

    target = 'https://iso.builds.garudalinux.org/iso/'
    
    exclude = ['unmaintained', 'latest']

    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
