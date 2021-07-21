from public import *  # noqa


def init():

    array = []
    base_urls = [
        "https://manjaro.org/downloads/official/gnome",
        "https://manjaro.org/downloads/official/kde",
        "https://manjaro.org/downloads/official/xfce",
        "https://manjaro.org/downloads/community/cinnamon",
        "https://manjaro.org/downloads/community/deepin",
        "https://manjaro.org/downloads/community/i3",
        "https://manjaro.org/downloads/community/mate"
    ]

    for base_url in base_urls:

        html = bs(requests.get(base_url).text, "html.parser")

        for target in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = target["href"]
            iso_arch = "amd64"
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"/(\d+(.\d+(.\d+)?)?)/", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
