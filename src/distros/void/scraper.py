from helpers import *

info = {
    'name': 'Void Linux',
    'url': 'https://voidlinux.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d{8})')
    url_base = 'https://mirror.yandex.ru/mirrors/voidlinux/live/current/'

    for iso_url in get.urls(url_base):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
