from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/mirrors/deepin/releases"

    html = bs(requests.get(base_url).text, "html.parser")

    iso_version = html.find_all("a", {"href": re.compile("^.*/$")})[-1]["href"][:-1]
    iso_url = f"{base_url}/{iso_version}/deepin-desktop-community-{iso_version}-amd64.iso"
    iso_arch = get_iso_arch(iso_url)
    iso_size = get_iso_size(iso_url)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
