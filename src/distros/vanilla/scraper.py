from shared import *

info = ns(
    name='Vanilla OS',
    url='https://vanillaos.org',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'\.(\d+)\.')
    
    target = 'https://github.com/Vanilla-OS/live-iso/releases/latest'

    for url, size in get.urls(target):

        arch = 'amd64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values