from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/slackware/slackware-iso"
    subpaths = [
        "slackware64-13.37-iso",
        "slackware64-14.2-iso",
        "slackware-12.2-iso",
        "slackware-13.37-iso",
        "slackware-14.2-iso"
    ]

    for subpath in subpaths:

        path = f"{base_url}/{subpath}"
        html = bs(requests.get(path).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*dvd.iso$")}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = "x86_64" if "slackware64" in filename else "i386"
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+.\d+)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
