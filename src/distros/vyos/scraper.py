from public import *  # noqa


base_urls = [
    "https://downloads.vyos.io/?dir=rolling/current/amd64/",
    "https://downloads.vyos.io/?dir=rolling/equuleus/amd64/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith(".iso") and "latest.iso" not in filename:
                iso_url = "https://downloads.vyos.io/" + filename
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                iso_version = re.search("\d+\.\d+", iso_url).group(0)
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
