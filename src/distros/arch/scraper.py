from helpers import *

info = {
    'name': 'Arch Linux',
    'url': 'https://archlinux.org'
}

def init():

    values = []
    exceptions = ['arch/', 'latest/', 'archlinux-x86_64']
    regexp_version = re.compile(r'-(\d+.\d+(.\d+)?)')
    url_base = 'https://mirror.yandex.ru/archlinux/iso/'

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      recursive=True):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
