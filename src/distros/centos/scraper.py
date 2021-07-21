from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/centos"
    subpaths = [
        "8/isos/x86_64",
        "8/isos/ppc64le",
        "8/isos/aarch64",
        "8-stream/isos/x86_64",
        "8-stream/isos/ppc64le",
        "8-stream/isos/aarch64",
        "7/isos/x86_64"
    ]

    for subpath in subpaths:

        path = f"{base_url}/{subpath}"
        html = bs(requests.get(path).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"(\d{8})", iso_url).group(1) \
                if "stream" in subpath \
                else re.search(r"OS-(\d+(.\d+(.\d+)?)?)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
