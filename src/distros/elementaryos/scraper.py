from public import *  # noqa


base_url = "https://elementary.io/"


def init():
    array = []
    html = str(bs(requests.get(base_url).text, "html.parser"))
    iso_url = "https:" + re.search(r'href="(//.*elementary.io/.*.iso)">',
                                   html).group(1)
    iso_arch = "x86_64"
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"-(\d+(.\d+(.\d+)?)?)", iso_url).group(1)
    array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
