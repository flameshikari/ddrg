from shared import *

info = ns(
    name='Qubes',
    url='https://qubes-os.org',
)

@scraper
def init():
    values = []

    regexp = r'Qubes-R(((\d+(\.\d+(\.\d+)?)?)(-[abr]\w+)?)?)'

    target = 'https://mirrors.edge.kernel.org/qubes/iso/'
    
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
