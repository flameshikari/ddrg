from shared import *

info = ns(
    name='antiX Linux',
    url='https://antixlinux.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)[-|_]'

    target = 'https://sourceforge.net/projects/antix-linux/files/Final/'
    
    exclude = ['archlinux-x86_64', 'arch/', 'latest/']

    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
