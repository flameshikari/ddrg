from public import *  # noqa

@test
def init():

    values = []

    iso_url = get.urls('https://disk.yandex.ru/d/YHflGF3zn3vf3w/DriveDroid.img')
    iso_size = get.size(iso_url)
    iso_version = 'Boot Tester'

    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
