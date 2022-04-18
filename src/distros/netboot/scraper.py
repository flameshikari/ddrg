from public import *  # noqa


def init():

    values = []
    url_version = 'https://api.github.com/repos/netbootxyz/netboot.xyz/releases/latest'

    iso_url = 'https://boot.netboot.xyz/ipxe/netboot.xyz.iso'
    iso_arch = get.arch(iso_url)
    iso_size = get.size(iso_url)
    iso_version = json.loads(rq.get(url_version).text)['tag_name']
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
