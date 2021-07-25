from public import *  # noqa


def init():

    array = []
    base_url = "https://bike.seedhost.eu/arcolinux/iso/"

    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile("^.*\.iso$")

    for target in html.find_all("a", {"class": "name", "href": regex}):

        iso_url = f"{base_url}{target['href'][2:]}"
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"v(\d+\.\d+\.\d+)", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
