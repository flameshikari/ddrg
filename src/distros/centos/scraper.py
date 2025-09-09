from shared import *

info = ns(
    name='CentOS',
    url='https://centos.org',
)

@scraper
def init():
    values = []

    regexp = r'/(\d+(\.\d+(\.\d+)?)?)(-\w+)?/'

    target = [
        'https://mirror.yandex.ru/centos/centos/',
        'https://mirror.yandex.ru/centos-stream/',
        'https://mirror.yandex.ru/centos/altarch/',
    ]

    exclude = [
        'AppStream/',
        'atomic/',
        'centosplus/',
        'cloud/',
        'COMPOSE_ID',
        'configmanagement/',
        'contrib/',
        'cr/',
        'core/',
        'CRB/',
        'debug/',
        'Devel/',
        'dotnet/',
        'extras/',
        'fasttrack/',
        'HighAvailability/',
        'infra/',
        'hyperscale/',
        'kmods/',
        'messaging/',
        'nfv/',
        'NFV/',
        'opstools/',
        '/os/',
        'paas/',
        'PowerTools/',
        'rt/',
        'ResilientStorage',
        'RT/',
        'SIGs/',
        'SCL/',
        'sclo/',
        'Source/',
        'source/',
        'storage/',
        'updates/',
        'virt/',
        'kernel/',
        'xen/',
        'experimental/',
        'epel/',
    ]
    
    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp).replace('-', ' ')

        version = f'Stream {version}' if 'Stream' in url else version

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
