from shared import *

info = ns(
    name='Absolute Linux',
    url='https://absolutelinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)'
    
    target = 'https://slackware.uk/absolute/'
    
    exclude = ['live']

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