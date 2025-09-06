from helpers import *

info = {
    'name': 'Ultimate Boot CD',
    'url': 'https://ultimatebootcd.com'
}

def init():

    values = []
    regexp_version = re.compile(r'(\d+).iso')
    url_base = 'http://mirror.koddos.net/ubcd/'

    for iso_url in get.urls(url_base, recursive=True, exclude=['ubcdlive']):
        iso_arch = 'bios'
        iso_size = get.size(iso_url)
        iso_version = '.'.join(list(re.search(regexp_version, str(iso_url)).group(1)))
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
