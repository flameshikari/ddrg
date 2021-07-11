from public import *  # noqa


base_url = "https://mirror.yandex.ru/fedora/linux/releases/"

subdirs = [
    "Everything/aarch64/",
    "Everything/armhfp/",
    "Everything/x86_64/",
    "Server/aarch64/",
    "Server/armhfp/",
    "Server/x86_64/",
    "Silverblue/aarch64/",
    "Silverblue/x86_64/",
    "Spins/x86_64/",
    "Workstation/arch64/",
    "Workstation/x86_64/"
]


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for version in html.find_all("a"):
        version = version.get("href")
        if version.startswith("3"):
            for subdir in subdirs:
                url = base_url + version + subdir + "iso/"
                html = bs(requests.get(url).text, "html.parser")
                for filename in html.find_all("a"):
                    filename = filename.get("href")
                    if filename.endswith(".iso"):
                        iso_url = url + filename
                        iso_arch = get_iso_arch(iso_url)
                        iso_size = get_iso_size(iso_url)
                        iso_version = re.search(r"-(\d+-\d+.\d+)",
                                                iso_url).group(1)
                        array.append((iso_url, iso_arch,
                                      iso_size, iso_version))
    return array
