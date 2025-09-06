from helpers import *

info = {
    'name': 'ALT Linux',
    'url': 'https://altlinux.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d+(\.\d+)?)-')
    url_bases = [
        'https://getalt.org/en/alt-workstation/',
        'https://getalt.org/en/alt-kworkstation/',
        'https://getalt.org/en/alt-server/',
        'https://getalt.org/en/alt-server-v/',
        'https://getalt.org/en/alt-education/',
        'https://getalt.org/en/simply/',
        'https://getalt.org/en/alt-workstation/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base):

            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
        
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
