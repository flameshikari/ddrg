from main import *  # noqa


def init():

    values = []

    iso_url = get.urls('https://disk.yandex.ru/d/YHflGF3zn3vf3w/Victoria_3.52c.iso')
    iso_version = '3.52c'
    iso_arch = 'bios'
    iso_size = get.size(iso_url)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
