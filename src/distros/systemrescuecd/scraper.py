from shared import *

info = ns(
    name='SystemRescue',
    url='https://system-rescue.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(\.\d+)?)'

    target = 'https://sourceforge.net/projects/systemrescuecd/files/sysresccd-x86/'
    

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
