from helpers import *

info = {
    'name': 'Zorin OS',
    'url': 'https://zorinos.com'
}

def init():

    values = []
    regexp_version = re.compile(r'Zorin-OS-((\d+)\.?\d+)-')
    url_base = 'https://mirrors.edge.kernel.org/zorinos-isos/'

    for iso_url in get.urls(url_base, recursive=True):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
