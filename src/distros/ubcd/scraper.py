from public import *  # noqa


base_urls = [
    "https://ftp.cc.uoc.gr/mirrors/linux/ubcd/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith(".iso"):
                iso_url = base_url + filename
                iso_arch = "bios"
                iso_size = get_iso_size(iso_url)
                iso_version = ".".join(filter(str.isdigit, filename))
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
