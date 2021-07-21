from public import *  # noqa


def init():

    array = []
    base_url = "https://sourceforge.net/projects/archlabs-linux-minimo/rss?path=/ArchLabsMinimo"

    xml = bs(requests.get(base_url).text, "xml")

    for item in xml.find_all("item"):

        content = item.find("content")

        iso_url = content["url"][:-9]
        iso_arch = get_iso_arch(iso_url)
        iso_size = int(content["filesize"])
        iso_version = re.search(r"-(\d+.\d+.\d+)", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
