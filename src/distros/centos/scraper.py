from public import *  # noqa


base_urls = [
    "https://mirror.yandex.ru/centos/8/isos/x86_64/",
    "https://mirror.yandex.ru/centos/8/isos/ppc64le/",
    "https://mirror.yandex.ru/centos/8/isos/aarch64/",
    "https://mirror.yandex.ru/centos/8-stream/isos/x86_64/",
    "https://mirror.yandex.ru/centos/8-stream/isos/ppc64le/",
    "https://mirror.yandex.ru/centos/8-stream/isos/aarch64/",
    "https://mirror.yandex.ru/centos/7/isos/x86_64/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith(".iso"):
                iso_url = base_url + filename
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                if "Stream" in filename:
                    iso_verson = re.search(r"(\d{8})", iso_url).group(1)
                else:
                    iso_version = re.search(r"OS-(\d+(.\d+(.\d+)?)?)",
                                            iso_url).group(1)
                array.append((iso_url, iso_arch,
                              iso_size, iso_version))
    return array
