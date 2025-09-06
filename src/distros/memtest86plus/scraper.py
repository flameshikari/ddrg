from helpers import *

info = {
    'name': 'Memtest86+',
    'url': 'https://memtest.org'
}

def init():

    values = []
    iso_version = '7.20'
    regexp_version = re.compile(r'_(\d+\.\d+(\.\d+)?)_x')

    iso_urls = [
        f'https://disk.yandex.ru/d/YHflGF3zn3vf3w/mt86plus_{iso_version}_x86.iso',
        f'https://disk.yandex.ru/d/YHflGF3zn3vf3w/mt86plus_{iso_version}_x64.iso',
        f'https://disk.yandex.ru/d/YHflGF3zn3vf3w/mt86plus_grub_{iso_version}_x64.iso'
    ]

    for iso_url in iso_urls:

        iso_url = get.urls(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
    
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
