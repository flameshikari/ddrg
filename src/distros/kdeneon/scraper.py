from public import *  # noqa


def init():

    array = []
    base_url = "https://neon.kde.org/download"

    html = bs(requests.get(base_url).text, "html.parser")

    for target in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = target["href"]
        iso_arch = "amd64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d{8})", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
