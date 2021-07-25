from public import *  # noqa


def init():
    
    array = []
    base_url = "https://www.proxmox.com/downloads"
    mirror_url = "http://download.proxmox.com/iso"
    
    html = bs(requests.get(base_url).text, "html.parser")
    
    for filename in html.find_all("a", {"class": "element-download-type-iso",
                                        "title": re.compile("^.*\.iso$")}):
    
        filename = filename["title"][9:]
        iso_url = f"{mirror_url}/{filename}"
        iso_arch = "amd64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"_(\d+(\.\d+(-\d+)?)?)", filename) \
                        .group(1)
    
        array.append((iso_url, iso_arch, iso_size, iso_version))
    
    return array
