from public import *  # noqa


homepage = "https://garudalinux.org/downloads.html"


def init():
    array = []
    html = bs(requests.get(homepage).text, "html.parser")
    for link in html.find_all("a"):
        link = link.get("href")
        if link.endswith(".iso") and "sourceforge" in link:
            iso_url = link
            iso_arch = "amd64"
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+).iso", iso_url).group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
