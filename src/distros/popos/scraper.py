from shared import *

info = ns(
    name='Pop!_OS',
    url='https://pop.system76.com',
)

def get_urls():
    versions = ['24.04', '22.04']
    vendors = ['intel', 'nvidia']
    base = 'https://api.pop-os.org/builds'
    matrix = [f'{base}/{iso}/{arch}' for iso in versions for arch in vendors]
    return matrix

@scraper
def init():
    values = []

    regexp = r'_(\d+.\d+)_'

    target = get_urls()
    
    for url, size in get.urls(target, json=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
