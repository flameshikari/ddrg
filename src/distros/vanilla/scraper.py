from helpers import *

info = {
    'name': 'Vanilla OS',
    'url': 'https://vanillaos.org'
}

def init():

    values = []
    regexp_version = re.compile(r'\.(\d+)\.')
    url_base = 'https://github.com/Vanilla-OS/live-iso/releases/latest'

    for iso_url in get.urls(url_base):
        iso_arch = 'amd64'
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
