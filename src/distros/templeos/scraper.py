from helpers import *

info = {
    'name': 'TempleOS',
    'url': 'https://templeos.org'
}

def init():

    values = []
    url_base = 'https://templeos.org/Downloads/'

    for iso_url in get.urls(url_base):
    
        iso_size = get.size(iso_url)
        iso_arch = 'amd64'
        iso_version = '5.03'
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
