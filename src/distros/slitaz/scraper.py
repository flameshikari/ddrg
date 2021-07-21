from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.slitaz.org/iso/rolling/"
    version_url = "https://slitaz.org/en/"

    html = bs(requests.get(version_url).text, "html.parser")
    iso_version = re.search(r"SliTaz (\d+(.\d+)?)",
                            str(html.find_all("a"))).group(1)

    html = bs(requests.get(base_url).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = base_url + filename["href"]
        iso_size = get_iso_size(iso_url)
        if any(x in iso_url for x in ["rolling.iso", "loram.iso"]):
            iso_arch = "i386"
        else:
            iso_arch = "x86_64"

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
