from shared import *

info = ns(
    name='Clonezilla',
    url='https://clonezilla.org',
)

@scraper
def init():
    values = []

    regexp = r'(?:/|live-)(\d+\.\d+\.\d+-\d+|\d+-\w+)(?:/|-)'

    target = [
        'https://free.nchc.org.tw/clonezilla-live/stable/',
        'https://free.nchc.org.tw/clonezilla-live/alternative/stable/',
    ]
    
    exclude = ['testing', 'OldFiles', 'source/']

    for url, size in get.urls(target, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
