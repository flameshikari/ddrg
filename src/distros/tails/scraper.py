from main import *  # noqa


def init():

    values = []
    exceptions = ['wikimedia']
    regexp_version = re.compile(r'-(\d+\.\d+)')
    url_base = 'https://tails.boum.org/install/download/index.en.html'

    for iso_url in get.urls(url_base, exclude=exceptions):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
