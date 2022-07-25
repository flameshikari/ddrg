from main import *  # noqa


def init():

    values = []
    iso_urls = [
        'https://templeos.org/Downloads/TempleOS.ISO',
        'https://templeos.org/Downloads/TempleOSLite.ISO'
    ]

    for iso_url in iso_urls:
    
        iso_size = get.size(iso_url)
        iso_arch = 'amd64'
        iso_version = '5.03'
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
