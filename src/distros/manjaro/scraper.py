from shared import *

info = ns(
    name='Manjaro',
    url='https://manjaro.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(.\d+)?)'

    target = [
        'https://manjaro.org/products/download/x86',
        'https://manjaro-sway.download/'
    ]
    
    for url, size in get.urls(target):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
