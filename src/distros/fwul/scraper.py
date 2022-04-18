from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'v(\d+.\d+)')
    url_base = 'https://leech.binbash.rocks:8008/mAid/stable/'

    for iso_url in get.urls(url_base, recurse=True):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
