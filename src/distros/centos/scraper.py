from helpers import *

info = {
    'name': 'CentOS',
    'url': 'https://centos.org'
}

def init():

    values = []
    exceptions = [
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
    # regexp_version = re.compile(r'-(\d+(\.\d+([\.|\-]\d+)?)?|Stream-\d+(-\d+)?)-')
    regexp_version = re.compile(r'/?(\d+\.\d+(\.\d+)?|Stream-\d+(-\d+)?)/?')
    url_bases = [
        'https://mirror.yandex.ru/centos/centos/',
        'https://mirror.yandex.ru/centos-stream/',
        'https://mirror.yandex.ru/centos/altarch/',
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions, recursive=True):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1).replace('-', ' ')
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
