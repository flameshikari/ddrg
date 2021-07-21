from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/sabayon/iso/monthly"
    version_url = "https://mirror.yandex.ru/sabayon/iso/monthly/LATEST_IS"

    iso_version = requests.get(version_url).text.split()[0]
    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile(rf"^.*{iso_version}.*\.iso$")

    for filename in html.find_all("a", {"href": regex}):

        iso_url = f"{base_url}/{filename['href']}"
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
