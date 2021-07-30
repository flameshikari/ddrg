from public import *  # noqa


def init():

    array = []
    base_url = "https://alpinelinux.org/downloads"

    html = bs(requests.get(base_url).text, "html.parser")

    for target in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = target["href"]
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d+.\d+(.\d+)?)", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
