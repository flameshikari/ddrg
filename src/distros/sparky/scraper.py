from shared import *

info = ns(
    name='SparkyLinux',
    url='https://sparkylinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+)'

    target = [
        'https://sparkylinux.org/download/stable/',
        'https://sparkylinux.org/download/rolling/',
    ]
    
    exclude = [
        'repo',
        'torrents',
        'armhf',
        'arm64',
        'files',
    ]

    for url, size in get.urls(
        target,
        exclude=exclude + ['sourceforge.net'],
        follow=True,
        filter=r'^https://archive.org/.*\.iso$',
    ):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
