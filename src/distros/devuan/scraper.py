from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.math.princeton.edu/pub/devuan"
    subpaths_1 = [
        "devuan_beowulf",
        "devuan_chimaera",
    ]
    subpaths_2 = [
        "desktop-live",
        "installer-iso",
        "minimal-live"
    ]

    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile("^.*\.iso$")

    for subpath_1 in subpaths_1:
        for subpath_2 in subpaths_2:

            path = f"{base_url}/{subpath_1}/{subpath_2}"
            html = bs(requests.get(path).text, "html.parser")

            for filename in html.find_all("a", {"href": regex}):

                iso_url = f"{path}/{filename['href']}"
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                iso_version = re.search(r"_(\d+(.\d+(.\d+)?)?)", iso_url).group(1)

                array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
