from public import *  # noqa


def init():

    array = []
    version_url = "https://www.freebsd.org/releases"

    html = bs(requests.get(version_url).text, "html.parser")
    iso_version = re.search(r"Release (\d+(.\d+)?)", str(html)).group(1)

    base_url = "https://mirror.yandex.ru/freebsd/releases/ISO-IMAGES/{}"
    html = bs(requests.get(base_url.format(iso_version)).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = f"{base_url.format(iso_version)}/{filename['href']}"
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
