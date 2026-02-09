from shared import *

info = ns(
    name='OpenSUSE',
    url='https://opensuse.org',
)

@scraper
def init():
    values = []

    regexp = r'\/(\d+\.\d+)\/'

    target = [
        'https://ftp.sh.cvut.cz/opensuse/slowroll/',
        'https://ftp.sh.cvut.cz/opensuse/tumbleweed/',
        'https://ftp.sh.cvut.cz/opensuse/distribution/leap/',
        'https://ftp.sh.cvut.cz/opensuse/distribution/leap-micro/',
    ]
    
    exclude = [
        'repo',
        # 'appliances/',
        '-stable',
        '-current',
        # '-Media',
        '-Debug',
        '-Source',
        '-Current',
        'next',
        'src',
    ]

    filter = r'Build|Snapshot'

    for url, size in get.urls(target, recursive=True, exclude=exclude, filter=filter):

        arch = get.arch(url)
        
        try:
            version = get.version(url, regexp)
        except:
            if 'slowroll' in url: version = 'Slowroll'
            elif 'tumbleweed' in url: version = 'Tumbleweed'

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
