from shared import *

info = ns(
    name='Puppy Linux',
    url='https://puppylinux-woof-ce.github.io',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?(-\d+)?|\d+-\d+)\.'

    target = 'https://sourceforge.net/projects/pb-gh-releases/files/'
    
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
