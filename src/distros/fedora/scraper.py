from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/fedora/linux/releases"
    version_url = "https://getfedora.org/en/workstation/download"
    subpaths = [
        "Everything/aarch64",
        "Everything/armhfp",
        "Everything/x86_64",
        "Server/aarch64",
        "Server/armhfp",
        "Server/x86_64",
        "Silverblue/aarch64",
        "Silverblue/x86_64",
        "Spins/x86_64",
        "Workstation/arch64",
        "Workstation/x86_64"
    ]

    html = bs(requests.get(version_url).text, "html.parser")
    version = re.search(r"Fedora (\d+) Workstation", str(html)).group(1)

    html = bs(requests.get(base_url).text, "html.parser")

    for subpath in subpaths:

        path = f"{base_url}/{version}/{subpath}/iso"
        html = bs(requests.get(path).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+-\d+.\d+)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
