from public import *  # noqa


base_urls = [
    "https://ftp.acc.umu.se/mirror/chakralinux.org/releases/",
    "https://ftp.acc.umu.se/mirror/chakralinux.org/releases/testing/"
]


def init():
    array = []
    years = [str(x) for x in [*range(2015, 2018), 2019]]
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith(".iso") and \
            any(x in filename for x in years):
                iso_url = base_url + filename
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                iso_version = re.search(r"chakra-(\d{4}.\d{2}(.\d{2})?)",
                                        iso_url).group(1)
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
