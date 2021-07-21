from public import *  # noqa


def init():

    array = []
    base_url = "https://www.gentoo.org/downloads/"
    mirror_url = "https://mirror.yandex.ru/gentoo-distfiles/releases/"

    html = bs(requests.get(base_url).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = re.sub(r"https.*releases/", mirror_url, filename["href"])
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d+)T", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
