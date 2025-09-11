from shared import *

info = ns(
    name='Xubuntu',
    url='https://xubuntu.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)'
    
    target = 'https://mirror.yandex.ru/ubuntu-cdimage/xubuntu/releases/'

    exclude = ['snapshot']
    
    pattern = r'releases\/(\w+)\/'

    for url, size in get.urls(target,
                              recursive=True,
                              pattern=pattern,
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