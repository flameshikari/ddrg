from helpers import *

info = {
    'name': 'Knoppix',
    'url': 'https://knopper.net/knoppix'
}

def init():

    values = []
    exceptions = [
        '-DE',
        'knoppix-',
        'contribs',
        'qemu',
        '-old'
    ]
    regexp_version = re.compile(r'KNOPPIX_V(\d+(\.\d+(\.\d+)?)?)')
    url_base = 'https://mirror.yandex.ru/knoppix/'

    for iso_url in get.urls(url_base, exclude=exceptions, recursive=True):
        
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
