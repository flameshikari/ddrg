from main import *  # noqa


def init():

    values = []
    exceptions = ['cd', 'CD'] + [f"_{str(i)}." for i in range(1, 4)]
    regexp_version = re.compile(r'_(\d+(\.\d+(\.\d+)?)?)')
    url_base = 'https://mirror.math.princeton.edu/pub/devuan/'

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      recurse=True):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
