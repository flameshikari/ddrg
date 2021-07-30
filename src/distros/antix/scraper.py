from public import *  # noqa


def init():

    array = []
    version_url = "https://antixlinux.com/download/"
    html = bs(requests.get(version_url).text, "html.parser")

    regex = re.compile("https://sourceforge.net.*")
    base_url = html.find("a", {"href": regex})["href"] \
                   .replace("files/", "rss?path=/")
    
    xml = bs(requests.get(base_url).text, "xml")

    for item in xml.find_all("item"):
        content = item.find("content")
        iso_url = content["url"][:-9]

        if iso_url.endswith(".iso"):

            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+\.\d+(\.\d+)?)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
