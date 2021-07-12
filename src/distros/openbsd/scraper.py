from public import *  # noqa


base_url = "https://www.openbsd.org/faq/faq4.html"


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for link in html.find_all("a"):
        link = link.get("href")
        if url.endswith(".iso"):
            iso_url = link
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"OpenBSD/(\d+.\d+)/", iso_url).group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
