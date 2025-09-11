from shared import *

info = ns(
    name='VyOS',
    url='https://vyos.org',
)

@scraper
def init():
    values = []

    regexp = r'download/(.*)/vyos'
    
    target = 'https://vyos.net/get/nightly-builds/'

    pattern = r'.*\.iso'

    for url, size in get.urls(target, pattern=pattern):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
