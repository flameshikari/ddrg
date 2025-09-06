from helpers import *

info = {
    'name': 'Parrot OS',
    'url': 'https://parrotlinux.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d+(.\d+(.\d+)?)?)')
    url_base = 'https://deb.parrot.sh/direct/parrot/iso/'
    exclude = [
        'zorin', 'caine',
        '/4.', '/5.',
        'current', 'testing'
    ]

    for iso_url in get.urls(url_base, recursive=True, exclude=exclude):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
