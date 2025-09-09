from shared import *

info = ns(
    name='Proxmox',
    url='https://proxmox.com',
)

@scraper
def init():
    values = []

    regexp = r'_(\d+(\.\d+(-\d+)?)?)'

    target = 'https://enterprise.proxmox.com/iso/'
    
    for url, size in get.urls(target):

        arch = 'amd64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
