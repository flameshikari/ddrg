from public import *  # noqa


def init():

    array = []
    version_url = "https://zorinos.com/download"

    html = bs(requests.get(version_url).text, "html.parser")
    version = re.search(r"Zorin OS ((\d+).\d+)", str(html))

    iso_version = version.group(1)
    base_version = version.group(2)

    base_url = "https://mirrors.edge.kernel.org/zorinos-isos/" + base_version
    html = bs(requests.get(base_url.format(base_version)).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = f"{base_url}/{filename['href']}"
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
