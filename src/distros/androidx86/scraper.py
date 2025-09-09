from shared import *

info = ns(
    name='Android-x86',
    url='https://android-x86.org',
)

@scraper
def init():
    values = []

    regexp = r'-v?(\d+(\.\d+)?)'
    
    target = 'https://sourceforge.net/projects/android-x86/files/'

    exclude = ['/Testing/']

    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values