from shared import *

info = ns(
    name='DriveDroid',
    url='https://github.com/FrozenCow/drivedroid-image',
)

@scraper
def init():
    values = []

    target = 'stash:drivedroid'

    for url, size in get.urls(target):

        arch = 'x86_64'
        version = 'Boot Tester'

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values