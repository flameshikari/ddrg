from helpers import *

info = {
    'name': 'ROSA',
    'url': 'https://rosalinux.ru'
}

def init():

    values = []

    regexp_version = re.compile(r'^.*\/iso\/\w+\.\w+\.R?(\d+(\.\d+)?)')
    url_base = 'https://www.rosalinux.ru/rosa-linux-download-links/'

    for iso_url in get.urls(url_base):

        iso_url = re.sub(r'rosa\w+\.ru', 'yandex.ru', iso_url)
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
