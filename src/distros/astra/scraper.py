from helpers import *

info = {
    'name': 'Astra Linux',
    'url': 'https://astralinux.ru'
}

def init():

    values = []
    exceptions = ['repository', '-stable', 'smolensk', 'leningrad', 'current']
    regexp_url = re.compile(r'.*\d+\.\d+.*')
    regexp_version = re.compile(r'-(\d+\.\d+(\.\d+(\.\d+)?)?)-')
    url_base = 'https://mirror.yandex.ru/astra/stable/'

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      pattern=regexp_url,
                                      recursive=True):
        iso_arch = 'x86_64'
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
