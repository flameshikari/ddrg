from shared import *

info = ns(
    name='Parrot OS',
    url='https://parrotlinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(.\d+(.\d+)?)?)'

    target = 'https://deb.parrot.sh/direct/parrot/iso/'
    
    exclude = ['zorin/', 'caine/', '/4.', '/5.']

    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
