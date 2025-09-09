from shared import *

info = ns(
    name='SliTaz',
    url='http://slitaz.org',
)

@scraper
def init():
    values = []

    regexp = r'\/iso\/(\d+.\d+|\w+)\/'

    target = 'https://mirror.slitaz.org/iso/'
    
    exclude = ['packages-', '-stable', '-rc', '/stable/', '/latest/']

    for url, size in get.urls(target, 
                              exclude=exclude,
                              recursive=True,
                              follow=False):

        arch = get.arch(url)
        version = get.version(url, regexp).capitalize()

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values