from shared import *

info = ns(
    name='FreeDOS',
    url='https://freedos.org',
)

@scraper
def init():
    values = []

    regexp = r'.*\/(\d+\.\d+)\/.*'

    target = 'https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/'
    
    exclude = [
        'pre-',
        'test',
        'tools',
        'unofficial',
        'previews',
        'repos',
        '1.0',
        'src',
    ]

    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = 'i386'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
