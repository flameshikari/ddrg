from shared import *

info = ns(
    name='Astra Linux',
    url='https://astralinux.ru',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+(\.\d+)?)?)-'

    target = 'https://mirror.yandex.ru/astra/stable/'
    
    exclude = [
        'repository',
        '-stable',
        'smolensk',
        'leningrad',
        'current',
    ]

    pattern = r'.*\d+\.\d+.*'

    for url, size in get.urls(target,
                              exclude=exclude,
                              pattern=pattern,
                              recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
