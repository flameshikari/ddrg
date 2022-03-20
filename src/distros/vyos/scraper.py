from public import *  # noqa


def init():

    array = []
    iso_urls = []
    base_urls = [
        "https://vyos.net/get/nightly-builds",
        "https://vyos.net/get/snapshots"
    ]

    for base_url in base_urls:

        html = bs(requests.get(base_url).text, "html.parser")

        iso_url = html.find_all("ul")[0].find_all("a")[0]["href"]
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"vyos-(\d+.\d+(.\d+)?)",
                                iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
