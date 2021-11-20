from public import *  # noqa


def init():

    array = []
    base_url = "https://garudalinux.org/downloads.html"

    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile("^.*mirrors.fossho.st.*\.iso$")

    for target in html.find_all("a", {"href": regex}):

        iso_url = target["href"]
        iso_arch = "amd64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d+).iso", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
