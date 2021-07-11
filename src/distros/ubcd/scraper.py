from public import *  # noqa


base_url = "https://mirror.clientvps.com/ubcd/"


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for filename in html.find_all("a"):
        filename = filename.get("href")
        if filename.endswith(".iso"):
            iso_url = base_url + filename
            iso_arch = "bios"
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"(\d+(\w+)?)\.iso", iso_url).group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
