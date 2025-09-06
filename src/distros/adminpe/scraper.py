from helpers import *

info = {
    'name': 'AdminPE',
    'url': 'https://adminpe.ru'
}

def init():

    values = []
    regexp_version = re.compile(r'_(\d+(\.\d+)?).img')

    iso_url = get.urls('https://disk.yandex.ru/d/YHflGF3zn3vf3w/admin-pe_4.4.img')
    iso_version = re.search(regexp_version, iso_url).group(1)
    iso_arch = 'x86_64'
    iso_size = get.size(iso_url)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
