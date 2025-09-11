from shared import *

info = ns(
    name='Strelec WinPE',
    url='https://sergeistrelec.name',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'_(\d+\.\d+\.\d+)_')
    
    target = 'yandex:strelec'

    for url, size in get.urls(target):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values