from shared import *

info = ns(
    name='Gentoo',
    url='https://gentoo.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+)T'

    archs = [
        'alpha', 'amd64', 'arm', 'arm64',
        'hppa', 'loong', 'm68k', 'mips',
        'ppc', 'riscv', 's390', 'sparc', 'x86'
    ]

    
    for arch in archs:

        target = f'https://www.gentoo.org/downloads/{arch}/'

        for url, size in get.urls(target):

            arch = get.arch(url)
            version = get.version(url, regexp)

            values.append(ns(
                arch=arch,
                size=size,
                url=url,
                version=version
            ))

    return values
