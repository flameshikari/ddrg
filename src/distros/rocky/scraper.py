from shared import *

info = ns(
    name='Rocky Linux',
    url='https://rockylinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+(\.\d+)?)-'
    
    target = 'https://download.rockylinux.org/pub/rocky/'
    
    exclude = [
        'AppStream/',
        'BaseOS/',
        'CRB/',
        'HighAvailability/',
        'NFV/',
        'RT/',
        'SAP/',
        'SAPHANA/',
        'PowerTools/',
        'ResilientStorage/',
        'Devel/',
        'devel/',
        'extras/',
        'images/',
        'metadata/',
        'nfv/',
        'plus/',
        '-latest',
    ]

    for url, size in get.urls(target, recursive=True, exclude=exclude):

        arch = get.arch(url)
        
        try:
            version = get.version(url, regexp)
        except:
            continue

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values