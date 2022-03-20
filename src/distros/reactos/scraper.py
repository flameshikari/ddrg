from public import *  # noqa


def init():

    array = []
    version_url = "https://reactos.org/download"
    base_url = "https://getfile.dokpub.com/yandex/get"
    iso_urls = [
        "https://disk.yandex.ru/d/YHflGF3zn3vf3w/ReactOS_Boot-{}.iso",
        "https://disk.yandex.ru/d/YHflGF3zn3vf3w/ReactOS_Live-{}.iso"
    ]

    iso_version = "0.4.14"
    iso_arch = "x86_64"

    for iso_url in iso_urls:
    
        iso_url = f"{base_url}/{iso_url.format(iso_version)}"
        iso_size = get_iso_size(iso_url)
    
        array.append((iso_url, iso_arch, iso_size, iso_version))
    
    return array
