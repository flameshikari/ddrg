from shared import *

info = ns(
    name='ReactOS',
    url='https://reactos.org',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'_(\d+\.\d+\.\d+)_')
    
    target = 'stash:reactos'

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