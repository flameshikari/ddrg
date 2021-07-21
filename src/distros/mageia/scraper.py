from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/mageia/iso"
    version_url = "https://www.mageia.org/en/downloads"

    subpaths = [
        "Mageia-{0}-Live-GNOME-x86_64",
        "Mageia-{0}-Live-Plasma-x86_64",
        "Mageia-{0}-Live-Xfce-i586",
        "Mageia-{0}-Live-Xfce-x86_64",
        "Mageia-{0}-i586",
        "Mageia-{0}-x86_64"
    ]

    html = bs(requests.get(version_url).text, "html.parser")
    iso_version = re.search(r"Mageia (\d+)", str(html)).group(1)

    for subpath in subpaths:

        arch = subpath.format(iso_version)
        filename = f"{arch}.iso"

        iso_url = f"{base_url}/{iso_version}/{arch}/{filename}"
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
