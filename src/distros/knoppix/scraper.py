from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/knoppix/DVD"
    version_url = "https://www.knopper.net/knoppix-mirrors/index-en.html"

    html = bs(requests.get(version_url).text, "html.parser")
    iso_version = re.search(r"KNOPPIX (\d+(.\d+)?)", str(html)).group(1)

    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile(rf"^.*{iso_version}.*\.iso$")

    for filename in html.find_all("a", {"href": regex}):

        iso_url = f"{base_url}/{filename['href']}"
        iso_arch = "x86_64"
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
