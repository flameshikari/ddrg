from helpers import *

info = {
    'name': 'SparkyLinux',
    'url': 'https://sparkylinux.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+)')
    target = 'https://sourceforge.net/projects/sparkylinux/files/'

    for iso_url in get.urls(target):
        iso_size = iso_url['size']
        iso_url = iso_url['url']
        iso_arch = get.arch(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
