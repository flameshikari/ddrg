from shared import *

info = ns(
    name='Fedora',
    url='https://getfedora.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+[.-]\d+\.\d+)'

    target = [
        'https://mirror.yandex.ru/fedora/linux/releases/',
    ]

    exclude = [
        'images/',
        'test/',
        'debug/',
        'os/',
        'source/',
        'images/',
        'Cloud/',
        'Container/',
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
