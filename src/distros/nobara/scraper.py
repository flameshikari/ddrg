from shared import *

info = ns(
    name='Nobara',
    url='https://nobaraproject.org',
)

@scraper
def init():
    values = []

    regexp = r'Nobara-(\d+)-'

    target = 'https://nobaraproject.org/download.html'
    
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
