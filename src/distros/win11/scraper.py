from shared import *

info = ns(
    name='Windows 11',
    url='https://microsoft.com/software-download/windows11',
)

@scraper
def init():
    values = []

    regexp = r'\.(\d+h\d+)_'
    regexp_lang = r'_([a-z]+-[a-z]+(-[a-z]+)?)\.iso'
    
    targets = [
        'https://massgrave.dev/windows_11_links',
        'https://massgrave.dev/windows_arm_links',
    ]

    for target in targets:
        for url, size in get.urls(target):

            arch = get.arch(url)
            version = f'{get.version(url, regexp).upper()} ({get.version(url, regexp_lang)})'

            values.append(ns(
                arch=arch,
                size=size,
                url=url,
                version=version
            ))

    return values