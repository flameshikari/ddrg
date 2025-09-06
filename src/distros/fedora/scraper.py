from helpers import *

info = {
    'name': 'Fedora',
    'url': 'https://getfedora.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d+[.-]\d+\.\d+)')
    excludes = [
        'images/',
        'test/',
        'debug/',
        'os/',
        'source/',
        'images/',
        'Cloud/',
        'Container/',
    ]
    url_bases = [
        'https://mirror.yandex.ru/fedora/linux/releases/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, recursive=True, exclude=excludes):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
