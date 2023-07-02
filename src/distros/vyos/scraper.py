from main import *  # noqa


def init():

    values = []
    exceptions = ['latest.iso']
    regexp_url = re.compile(r'.*\.iso')
    regexp_version = re.compile(r'vyos-(\d+\.\d+(\.\d+)?)')
    regexp_version_extra = re.compile(r'([S0-9]+)-amd64')

    url_bases = [
        'https://vyos.net/get/nightly-builds/',
        'https://vyos.net/get/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions,
                                          pattern=regexp_url):
            iso_size = get.size(iso_url)
            if iso_size is None: continue
            iso_arch = get.arch(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1) + ' ' + \
                          re.search(regexp_version_extra, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
