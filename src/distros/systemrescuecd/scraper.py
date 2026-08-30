from shared import *

info = ns(
    name='SystemRescue',
    url='https://system-rescue.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)'

    target = 'https://www.system-rescue.org/Download/'
    

    for url, size in get.urls(
        target,
        exclude=['sourceforge.net'],
        follow=True,
        filter=r'^https://fastly-cdn.system-rescue.org/.*\.iso$',
    ):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
