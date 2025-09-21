from shared import *

info = ns(
    name='PikaOS',
    url='https://wiki.pika-os.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'

    target = 'https://wiki.pika-os.com/home'
    
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
