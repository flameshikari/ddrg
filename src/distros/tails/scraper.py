from public import *  # noqa


def init():

    array = []
    base_url = "https://mirrors.edge.kernel.org/tails/stable/tails-amd64-{0}/tails-amd64-{0}.iso"
    version_url = "https://tails.boum.org/index.en.html"

    html = bs(requests.get(version_url).text, "html.parser")
    version = html.find_all("a", {"href": "./install/index.en.html"})[1].text

    iso_version = re.search(r"Get Tails \n(\d+.\d+)", version).group(1)
    iso_url = base_url.format(iso_version)
    iso_arch = get_iso_arch(iso_url)
    iso_size = get_iso_size(iso_url)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
