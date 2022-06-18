from main import *  # noqa


def init():

    values = []
    exceptions = ['latest.iso']
    regexp_url = re.compile(r'.*\.iso')
    regexp_version = re.compile(r'vyos-(\d+\.\d+(\.\d+)?)')
    url_bases = [
        'https://vyos.net/get/nightly-builds/',
        'https://vyos.net/get/snapshots/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions,
                                          pattern=regexp_url,
                                          recurse=True):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
