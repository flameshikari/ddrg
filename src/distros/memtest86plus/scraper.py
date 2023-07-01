from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(\.\d+)?)-')

    iso_urls = [
        'https://disk.yandex.ru/d/YHflGF3zn3vf3w/mt86plus-6.20-x32.iso',
        'https://disk.yandex.ru/d/YHflGF3zn3vf3w/mt86plus-6.20-x64.iso',
        'https://disk.yandex.ru/d/YHflGF3zn3vf3w/mt86plus_grub-6.20-x64.iso'
    ]

    for iso_url in iso_urls:

        iso_url = get.urls(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        iso_arch = None
        iso_size = get.size(iso_url)
    
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
