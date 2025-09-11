from shared import *

info = ns(
    name='Slax',
    url='https://slax.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+(\.\d+)?)?)'

    target = 'https://ftp.cvut.cz/mirrors/slax/'
    
    exclude = ['old/', 'Debian', 'Slackware', 'source']

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