from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.clientvps.com/ubcd"
    version_url = "https://www.ultimatebootcd.com/download.html"

    html = bs(requests.get(version_url).text, "html.parser")

    iso_version = re.search(r"V(\d+(.\d+(.\d+)?)?)", str(html)).group(1)
    iso_url = f"{base_url}/ubcd{iso_version.replace('.', '')}.iso"
    iso_arch = "bios"
    iso_size = get_iso_size(iso_url)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
