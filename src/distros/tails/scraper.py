from shared import *

info = ns(
    name='Tails',
    url='https://tails.boum.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+)'
    
    target = 'https://tails.boum.org/install/download/index.en.html'

    exclude = ['wikimedia']

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