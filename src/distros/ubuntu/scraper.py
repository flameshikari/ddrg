from shared import *

info = ns(
    name='Ubuntu',
    url='https://ubuntu.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)-'
    
    target = 'https://mirror.yandex.ru/ubuntu-releases/releases/'

    pattern = r'\/releases\/\w+\/'

    exclude = [
        'netboot/', 'cdicons/', 'include/'
    ]

    for url, size in get.urls(target,
                              pattern=pattern,
                              recursive=True,
                              exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values