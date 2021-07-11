from public import *  # noqa


base_urls = [
    "https://sourceforge.net/projects/zorin-os/rss?path=/15/",
    "https://sourceforge.net/projects/zorin-os/rss?path=/16/beta/"
]


def init():
    array = []
    for base_url in base_urls:
        xml = bs(requests.get(base_url).text, "xml")
        values = xml.find_all("item")
        for i in values:
            content = i.find("content")
            iso_url = content["url"][:-9]
            iso_arch = get_iso_arch(iso_url)
            iso_size = int(content["filesize"])
            iso_version = re.search(r"OS-(\d+(.\d+)?)", iso_url).group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
