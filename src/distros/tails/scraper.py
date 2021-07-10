from public import *


base_urls = [
    "https://mirrors.edge.kernel.org/tails/stable/",
    "https://mirrors.edge.kernel.org/tails/alpha/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for version in html.find_all("a"):
            version = version.get("href")
            if version.startswith("tails"):
                iso_url = base_url + version + version[:-1] + ".iso"
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                iso_version = re.search(r"tails-amd64-(.*)/", version) \
                                .group(1)
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
