from helpers import *

info = {
    'name': 'KDE neon',
    'url': 'https://neon.kde.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d{8})')
    url_base = 'https://neon.kde.org/download'

    for iso_url in get.urls(url_base):
        iso_arch = 'amd64'
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
