from public import *  # noqa


base_url = "https://mirrors.edge.kernel.org/qubes/iso/"


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for filename in html.find_all("a"):
        filename = filename.get("href")
        if filename.endswith(".iso") and not \
        any(x in filename for x in ["rc", "alpha"]):
            iso_url = base_url + filename
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"Qubes-R(\d+(.\d+(.\d+)?)?)", iso_url) \
                            .group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
