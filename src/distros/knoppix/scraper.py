from shared import *

info = ns(
    name='Knoppix',
    url='https://knopper.net/knoppix',
)

@scraper
def init():
    values = []

    regexp = r'KNOPPIX_V(\d+(\.\d+(\.\d+)?)?)'

    target = 'https://mirror.yandex.ru/knoppix/'

    exclude = [
        '-DE',
        'knoppix-',
        'contribs',
        'qemu',
        '-old'
    ]

    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
