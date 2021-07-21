from public import *  # noqa


def init():

    array = []
    iso_urls = []
    base_urls = [
        "https://vyos.net/get/nightly-builds",
        "https://vyos.net/get/snapshots"
    ]

    html = bs(requests.get(base_urls[0]).text, "html.parser")
    for x in [0, 1]:
        iso_urls.append(html.find_all("ul")[x].find_all("a")[0]["href"])

    html = bs(requests.get(base_urls[1]).text, "html.parser")
    for x in html.find_all("a", {"href": re.compile("^.*\.iso$")}):
        iso_urls.append(x["href"])

    for iso_url in iso_urls:

        iso_arch = "amd64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"vyos-(\d+.\d+(.\d+(-rc\d+)?)?)",
                                iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
