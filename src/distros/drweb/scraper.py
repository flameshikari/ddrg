from shared import *

info = ns(
    name='Dr.Web LiveDisk',
    url='https://free.drweb.com/aid_admin/',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)-'

    target = 'https://free.drweb.com/aid_admin/'
    
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
