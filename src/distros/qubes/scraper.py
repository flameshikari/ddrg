from public import *  # noqa


def init():

    array = []
    base_url = "https://mirrors.edge.kernel.org/qubes/iso"
    version_url = "https://www.qubes-os.org"

    html = bs(requests.get(version_url).text, "html.parser")
    version = re.search(r"Version (((\d+).\d+).\d+)", str(html))

    html = bs(requests.get(base_url).text, "html.parser")
    regex = re.compile(fr"^.*Qubes-R((({version.group(3)}(.\d+(.\d+)?)?))(-[abr]\w+)?).*.iso$")

    for filename in html.find_all("a", {"href": regex}):

        iso_url = f"{base_url}/{filename['href']}"
        iso_version = re.search(regex, iso_url).group(1)
        if not check_version(iso_version) >= check_version(version.group(1)): continue
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array