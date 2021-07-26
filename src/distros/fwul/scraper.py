from public import *  # noqa


def init():

    array = []

    base_url = "https://leech.binbash.rocks:8008/mAid/stable"
    html = bs(requests.get(base_url).text, "html.parser")

    regex = re.compile("^.*\.iso$")
    filename = html.find_all("a", {"href": regex})[0]["href"]

    iso_url = f"{base_url}/{filename}"
    iso_arch = get_iso_arch(iso_url)
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"v(\d+.\d+)", iso_url).group(1)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
