from shared import *

info = ns(
    name='Slackware',
    url='http://slackware.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'

    target = 'https://mirror.yandex.ru/slackware-iso/'
    
    exclude = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'source']

    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = 'x86_64' if '64' in url else 'i386'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values