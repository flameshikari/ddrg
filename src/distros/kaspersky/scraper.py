from helpers import *

info = {
    'name': 'Kaspersky Rescue Disk',
    'url': 'https://kaspersky.com/downloads/free-rescue-disk'
}

def init():

    values = []
    regexp_version = re.compile(r'/(\d+)/krd.iso')

    iso_urls = [
        'https://rescuedisk.s.kaspersky-labs.com/updatable/2018/krd.iso',
        'https://rescuedisk.s.kaspersky-labs.com/updatable/2024/krd.iso'
    ]

    iso_arch = 'x86_64'

    for iso_url in iso_urls:
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)

        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
