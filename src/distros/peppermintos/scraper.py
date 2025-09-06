from helpers import *

info = {
    'name': 'Peppermint OS',
    'url': 'https://peppermintos.com'
}

def init():

    values = []
    regexp_version = re.compile(r'Release Notes for Peppermint (\d+)')
    url_base = 'https://sourceforge.net/projects/peppermintos/files/isos/'
    url_version = 'https://peppermintos.com/release-notes/'
    response = rq.get(url_version)
    iso_version = re.search(regexp_version, str(response.text)).group(1)

    for iso_url in get.urls(url_base):

        iso_size = iso_url['size']
        iso_url = iso_url['url']
        iso_arch = get.arch(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
