from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+(\.\d+(\.\d+)?)?)')
    url_base = 'https://mirror.truenetwork.ru/mxlinux-cd/MX/Final/'

    for iso_url in get.urls(url_base, recurse=True):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
