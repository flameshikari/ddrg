from public import *  # noqa


def init():

    array = []
    version_url = "https://zorinos.com/download"

    html = bs(requests.get(version_url).text, "html.parser")
    version = re.search(r"Zorin OS ((\d+).\d+)", str(html))

    iso_version = version.group(1)
    base_version = version.group(2)

    base_url = "https://sourceforge.net/projects/zorin-os/rss?path=/{}"
    xml = bs(requests.get(base_url.format(base_version)).text, "xml")

    for item in xml.find_all("item"):

        content = item.find("content")
        iso_url = content["url"][:-9]
        if iso_version not in iso_url: continue
        iso_arch = get_iso_arch(iso_url)
        iso_size = int(content["filesize"])

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
