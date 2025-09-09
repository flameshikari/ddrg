from shared import *

info = ns(
    name='KDE neon',
    url='https://neon.kde.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d{8})'

    target = 'https://neon.kde.org/download'
    
    for url, size in get.urls(target):

        arch = 'amd64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
