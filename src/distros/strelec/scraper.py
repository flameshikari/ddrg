from helpers import *

info = {
    'name': 'Strelec WinPE',
    'url': 'https://sergeistrelec.name'
}

def init():

    values = []
    regexp_version = re.compile(r'_(\d+\.\d+\.\d+)_')

    iso_url = get.urls('https://disk.yandex.ru/d/YHflGF3zn3vf3w/strelec-winpe-11-10-8_2025.04.24_x86_64.img')
    iso_version = re.search(regexp_version, iso_url).group(1)
    iso_arch = get.arch(iso_url)
    iso_size = get.size(iso_url)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
