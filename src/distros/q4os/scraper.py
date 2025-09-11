from shared import *

info = ns(
    name='Q4OS',
    url='https://q4os.org',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'-(\d+\.\d+)')
    
    target = 'https://sourceforge.net/projects/q4os/files/'
    
    exclude = [
        'experimental',
        'loopimage',
        'depreciated',
        'unofficial',
    ]

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