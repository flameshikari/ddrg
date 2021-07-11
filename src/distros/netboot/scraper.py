from public import *  # noqa


version_url = "https://api.github.com/repos/netbootxyz/netboot.xyz/" \
              "releases/latest"


def init():
    iso_url = "https://boot.netboot.xyz/ipxe/netboot.xyz.iso"
    iso_arch = "legacy+uefi"
    iso_size = get_iso_size(iso_url)
    iso_version = json.loads(requests.get(version_url).text)['tag_name']
    return [(iso_url, iso_arch, iso_size, iso_version)]
