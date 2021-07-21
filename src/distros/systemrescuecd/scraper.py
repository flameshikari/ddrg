from public import *  # noqa


def init():

    array = []
    base_url = "https://www.system-rescue.org/Download"

    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile("^.*\.iso/download$")

    for target in html.find_all("a", {"href": regex}):

        iso_url = target["href"][:-9]
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d+.\d+(.\d+)?)", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
