from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(-\d+\.\d+)?)')
    url_bases = [
        'https://www.truenas.com/download-truenas-core/',
        'https://www.truenas.com/download-truenas-scale/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base):
            iso_arch = 'amd64'
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
