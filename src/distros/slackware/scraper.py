from public import *  # noqa


def init():

    array = []
    base_url = "https://slackware.uk/slackware/slackware-iso"
    subpaths = [
        "slackware64-15.0-iso",
        "slackware-15.0-iso",
    ]

    for subpath in subpaths:

        path = f"{base_url}/{subpath}"
        html = bs(requests.get(path).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*dvd.iso$")}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = "x86_64" if "64" in iso_url else "i386"
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+.\d+)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
