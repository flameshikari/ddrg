from shared import *

info = ns(
    name='SparkyLinux',
    url='https://sparkylinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+)'

    target = 'https://sourceforge.net/projects/sparkylinux/files/'
    
    exclude = [
        'repo',
        'torrents',
        'armhf',
        'arm64',
        'files',
    ]

    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
