from helpers import *

info = {
    'name': 'Qubes',
    'url': 'https://qubes-os.org'
}

def init():

    values = []
    regexp_version = re.compile(r'Qubes-R(((\d+(\.\d+(\.\d+)?)?)(-[abr]\w+)?)?)')
    url_base = 'https://mirrors.edge.kernel.org/qubes/iso/'

    for iso_url in get.urls(url_base):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
