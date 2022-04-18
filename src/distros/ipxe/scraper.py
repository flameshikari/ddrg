from public import *  # noqa


def init():

    values = []
    url_version = 'https://api.github.com/repos/ipxe/ipxe/tags'

    iso_url = 'https://boot.ipxe.org/ipxe.iso'
    iso_arch = get.arch(iso_url)
    iso_size = get.size(iso_url)
    iso_version = json.loads(rq.get(url_version).text)[0]['name'][1:]
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values

