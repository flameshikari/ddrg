from public import *  # noqa


def init():

    array = []

    version_url = "https://api.github.com/repos/netbootxyz/netboot.xyz/releases/latest"

    iso_url = "https://boot.netboot.xyz/ipxe/netboot.xyz.iso"
    iso_arch = get_iso_arch(iso_url)
    iso_size = get_iso_size(iso_url)
    iso_version = json.loads(requests.get(version_url).text)["tag_name"]

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
