from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(-\d+)?)')
    url_base = f'https://sourceforge.net/projects/pb-gh-releases/files/'
    
    for iso_url in get.urls(url_base, recurse=True):
        iso_size = iso_url['size']
        iso_url = iso_url['url']
        iso_arch = get.arch(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
