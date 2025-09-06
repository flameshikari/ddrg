from helpers import *

info = {
    'name': 'Endless OS',
    'url': 'https://endlessos.com'
}

def init():

    values = []
    regexp_version = re.compile(r'/(\d+\.\d+\.\d+(\.\d+)?)/')
    url_base = 'https://images-cdn.endlessm.com/releases-eos-3.json'

    for iso_url in get.urls(url_base, pattern=r'\.base\.'):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
