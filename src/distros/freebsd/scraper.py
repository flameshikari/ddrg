from helpers import *

info = {
    'name': 'FreeBSD',
    'url': 'https://freebsd.org'
}

def init():

    values = []
    exceptions = ['-RC']
    regexp_version = re.compile(r'-(\d+(\.\d+)?)')
    url_base = 'https://mirror.yandex.ru/freebsd/releases/ISO-IMAGES/'

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      recursive=True):
        iso_version = re.search(regexp_version, iso_url).group(1)
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
