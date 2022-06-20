from main import *  # noqa


def init():

    values = []
    iso_version = "0.4.14"
    iso_arch = "x86_64"
    iso_urls = [
        f"https://disk.yandex.ru/d/YHflGF3zn3vf3w/ReactOS_Boot-{iso_version}.iso",
        f"https://disk.yandex.ru/d/YHflGF3zn3vf3w/ReactOS_Live-{iso_version}.iso"
    ]

    for iso_url in iso_urls:
        
        iso_url = get.urls(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
