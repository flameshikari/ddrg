from shared import *

info = ns(
    name='Oracle Linux',
    url='https://www.oracle.com/linux/',
)

@scraper
def init():
    values = []

    regexp = r'/(OL\d+/u\d+)/'

    base = 'https://yum.oracle.com/'
    target = 'https://yum.oracle.com/oracle-linux-isos.html'

    exclude = ['uek', 'src']
    
    for url, size in get.urls(target, exclude=exclude, add_base=base):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
