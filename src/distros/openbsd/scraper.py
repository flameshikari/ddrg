from shared import *

info = ns(
    name='OpenBSD',
    url='https://openbsd.org',
)

@scraper
def init():
    values = []

    regexp = r'OpenBSD/(\d+\.\d+)/'

    target = 'https://www.openbsd.org/faq/faq4.html'
    
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
