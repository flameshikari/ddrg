from shared import *

info = ns(
    name='Kubuntu',
    url='https://kubuntu.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)'

    target = 'https://mirror.yandex.ru/ubuntu-cdimage/kubuntu/releases/'
    
    exclude = ['questing']
    
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
