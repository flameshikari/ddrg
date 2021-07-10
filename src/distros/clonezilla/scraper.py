from public import *  # noqa


base_urls = [
    "https://sourceforge.net/projects/clonezilla/"
    "rss?path=/clonezilla_live_stable",
    "https://sourceforge.net/projects/clonezilla/"
    "rss?path=/clonezilla_live_alternative"
]


def init():
    array = []
    for base_url in base_urls:
        xml = bs(requests.get(base_url).text, "xml")
        values = xml.find_all("item")
        for i in values:
            content = i.find("content")
            iso_url = content["url"][:-9]
            if iso_url.endswith(".iso"):
                iso_arch = get_iso_arch(iso_url)
                iso_size = int(content["filesize"])
                if "stable" in iso_url:
                    iso_version = re.search(r"-(\d+.\d+.\d+-\d+)", iso_url) \
                                    .group(1)
                else:
                    iso_version = re.search(r"-(\d{8})", iso_url).group(1)
                array.append((iso_url, iso_arch, iso_size, iso_version))
            else:
                continue
    return array
