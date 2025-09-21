from shared import *

info = ns(
    name='Rescatux',
    url='https://www.supergrubdisk.org/rescatux/',
)

@scraper
def init():
    values = []

    regexp = r'[-|_](\d+\.\d+)'

    target = 'https://sourceforge.net/projects/rescatux/files/'
    
    exclude = [
        'chntpw',
        'legacy_downloads',
        'beta',
    ]

    for url, size in get.urls(target, exclude=exclude):

        arch = get.arch(url, 'i386') 
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
