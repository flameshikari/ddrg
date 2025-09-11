from shared import *

info = ns(
    name='PsychOS',
    url='https://psychoslinux.gitlab.io',
)

@scraper
def init():
    values = []

    regexp = r'(\d+.\d+.\d+).iso'

    target = 'https://psychoslinux.gitlab.io/downloads.html'
    
    for url, size in get.urls(target):

        arch = 'i486' if '486' in url else 'i686'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
