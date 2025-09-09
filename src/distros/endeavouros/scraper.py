from shared import *

info = ns(
    name='EndeavourOS',
    url='https://endeavouros.com',
)

@scraper
def init():
    values = []

    regexp = r'[-|_](\d+\.\d+\.\d+|\d+_\d+|\d+-\d+)'

    target = 'https://ftp.belnet.be/mirror/endeavouros/iso/'
    
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
