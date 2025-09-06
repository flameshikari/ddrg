from helpers import *

info = {
    'name': 'AlmaLinux',
    'url': 'https://almalinux.org'
}

def init():

    values = []
    exceptions = ['latest']
    regexp_version = re.compile(r'-(\d+(\.\d+)?)-')
    url_bases = [
        'https://mirror.yandex.ru/almalinux/8/isos/',
        'https://mirror.yandex.ru/almalinux/9/isos/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions,
                                          recursive=True):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
