from public import *  # noqa


base_url = "https://www.system-rescue.org/Download/"


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for filename in html.find_all("a"):
        filename = filename.get("href")
        if filename.endswith(".iso/download"):
            iso_url = filename[:-9]
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+.\d+(.\d+)?)", iso_url).group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
