from public import *  # noqa


def init():

    array = []
    base_url = "https://getfile.dokpub.com/yandex/get"
    iso_url = "https://disk.yandex.ru/d/YHflGF3zn3vf3w/AdminPE_UEFI-4.4.iso"
    
    iso_url = f"{base_url}/{iso_url}"
    iso_version = "4.4"
    iso_arch = "x86_64"
    iso_size = get_iso_size(iso_url)
    
    array.append((iso_url, iso_arch, iso_size, iso_version))
    
    return array
