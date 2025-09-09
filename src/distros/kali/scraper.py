from shared import *

info = ns(
    name='Kali Linux',
    url='https://kali.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d{4}.\w+)-'

    target = [
        'https://mirror.truenetwork.ru/kali-images/current/',
        'https://mirror.truenetwork.ru/kali-images/kali-weekly/'
    ]
    
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
