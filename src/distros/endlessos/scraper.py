from shared import *

info = ns(
    name='Endless OS',
    url='https://endlessos.com',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+\.\d+\.\d+(\.\d+)?)/'

    target = 'https://images-cdn.endlessm.com/releases-eos-3.json'

    pattern = r'\.base\.'
    
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
