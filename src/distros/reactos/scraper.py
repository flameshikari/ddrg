from public import *  # noqa

base_url = "https://reactos.org/download/"

iso_urls = [
    "https://hyperion.hexed.pw/pub/iso/reactos/ReactOS-{}.iso",
    "https://hyperion.hexed.pw/pub/iso/reactos/ReactOS-{}-Live.iso"
]


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    version = re.search(r'React<span.*">OS</span> (\d+.\d+.\d+)</h1>',
                        str(html)).group(1)
    for iso_url in iso_urls:
        iso_url = iso_url.format(version)
        iso_arch = "x86_64"
        iso_size = get_iso_size(iso_url)
        iso_version = version
        array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
