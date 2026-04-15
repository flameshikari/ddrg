from shared import *

info = ns(
    name='ZimaOS',
    url='https://zimaspace.com/zimaos',
)

@scraper
def init():
    values = []

    exclude = ['-alpha', '-beta']

    regexp = r'/(\d+\.\d+\.\d+(-\d+|\.\d+)?)/'

    target = 'github:IceWhaleTech/ZimaOS'

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