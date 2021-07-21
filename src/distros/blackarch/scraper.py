from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/mirrors/blackarch/iso"

    html = bs(requests.get(base_url).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = f"{base_url}/{filename['href']}"
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d{4}.\d{2}.\d{2})", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
