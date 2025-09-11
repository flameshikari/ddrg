from shared import *

info = ns(
    name='PCLinuxOS',
    url='https://pclinuxos.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'

    target = 'http://ftp.nluug.nl/pub/os/Linux/distr/pclinuxos/pclinuxos/iso/'
    
    for url, size in get.urls(target):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
