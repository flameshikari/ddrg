from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(-\d+)?)')
    distros = [
        'BionicPup32',
        'BookwormPup32',
        'BookwormPup64',
        'FocalPup32',
        'JammyPup32',
        'NoblePup32',
        'VoidPup32',
        'VoidPup64',
        'S15Pup32',
        'S15Pup64'
    ]

    for distro in distros:
        url_base = f'https://sourceforge.net/projects/pb-gh-releases/files/{distro}_release/'
        for iso_url in get.urls(url_base):
            iso_size = iso_url['size']
            iso_url = iso_url['url']
            iso_arch = get.arch(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
