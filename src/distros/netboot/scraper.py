from main import *  # noqa


def init():

    values = []
    iso_urls = [
      'https://boot.netboot.xyz/ipxe/netboot.xyz.iso',
      'https://boot.netboot.xyz/ipxe/netboot.xyz.img'
    ]
    url_version = 'https://api.github.com/repos/netbootxyz/netboot.xyz/releases/latest'
    iso_version = json.loads(rq.get(url_version).text)['tag_name']

    for iso_url in iso_urls:

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
