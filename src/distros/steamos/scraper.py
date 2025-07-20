from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(\.\d+)?).img')

    iso_urls = [
        'https://disk.yandex.ru/d/YHflGF3zn3vf3w/steamos_deck_20250521.10-3.7.7.img',
    ]

    for iso_url in iso_urls:

        iso_url = get.urls(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        iso_arch = 'amd64'
        iso_size = get.size(iso_url)
    
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
