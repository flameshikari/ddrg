from public import *  # noqa


base_urls = [
    "https://mirror.yandex.ru/slackware/slackware-iso/slackware64-13.37-iso/",
    "https://mirror.yandex.ru/slackware/slackware-iso/slackware64-14.2-iso/",
    "https://mirror.yandex.ru/slackware/slackware-iso/slackware-12.2-iso/",
    "https://mirror.yandex.ru/slackware/slackware-iso/slackware-13.37-iso/",
    "https://mirror.yandex.ru/slackware/slackware-iso/slackware-14.2-iso/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith("dvd.iso"):
                iso_url = base_url + filename
                iso_arch = "x86_64" if "slackware64" in filename else "i386"
                iso_size = get_iso_size(iso_url)
                iso_version = re.search(r"-(\d+.\d+)", iso_url).group(1)
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
