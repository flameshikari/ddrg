from helpers import *

info = {
    'name': 'Manjaro',
    'url': 'https://manjaro.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(.\d+)?)')
    url_bases = [
        'https://manjaro.org/products/download/x86',
        'https://manjaro-sway.download/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base):

            iso_arch = 'x86_64'
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
