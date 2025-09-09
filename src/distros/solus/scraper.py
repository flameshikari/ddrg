from shared import *

info = ns(
    name='Solus',
    url='https://getsol.us',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)-'

    target = 'https://getsol.us/download/'
    
    for url, size in get.urls(target):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values