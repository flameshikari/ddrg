from shared import *

info = ns(
    name='Bliss OS',
    url='https://blissos.org',
)

@scraper
def init():
    values = []

    regexp = r'-v(\d+\.\d+(\.\d+)?)'

    target = 'https://sourceforge.net/projects/blissos-x86/files/Official/'
    
    exclude = ['Archive']

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
