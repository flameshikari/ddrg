from public import *  # noqa


def init():

    array = []
    base_url = "https://sourceforge.net/projects/ophcrack/rss?path=/ophcrack-livecd/3.6.0"

    xml = bs(requests.get(base_url).text, "xml")

    for item in xml.find_all("item"):

        content = item.find("content")
        iso_url = content["url"][:-9]
        iso_arch = "x86_64"
        iso_size = int(content["filesize"])
        iso_version = "3.6.0"

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
