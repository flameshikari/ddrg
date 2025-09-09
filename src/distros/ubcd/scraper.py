from shared import *

info = ns(
    name='Ultimate Boot CD',
    url='https://ultimatebootcd.com',
)

@scraper
def init():
    values = []

    regexp = r'(\d+).iso'
    
    target = 'http://mirror.koddos.net/ubcd/'

    exclude = ['ubcdlive']

    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = 'i386'
        version =  '.'.join(list(get.version(url, regexp)))

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values