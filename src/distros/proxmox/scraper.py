from public import *  # noqa


def init():

    array = []
    base_url = "https://www.proxmox.com"

    html = bs(requests.get(f"{base_url}/downloads").text, "html.parser")

    for filename in html.find_all("a", {"title": re.compile("^.*\.iso$")}):

        iso_url = f"{base_url}{filename['href']}"
        iso_arch = "amd64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"_(\d+(\.\d+(-\d+)?)?)", filename["title"]) \
                        .group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
