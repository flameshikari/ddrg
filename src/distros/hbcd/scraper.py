from public import *  # noqa


def init():

    array = []
    version_url = "https://www.hirensbootcd.org/download"

    html = bs(requests.get(version_url).text, "html.parser")

    iso_url = "https://www.hirensbootcd.org/files/HBCD_PE_x64.iso"
    iso_arch = "amd64"
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"\(v(\d+(.\d+(.\d+)?)?)\)", str(html)).group(1)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
