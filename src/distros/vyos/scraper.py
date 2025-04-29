from main import *  # noqa


def init():

    values = []
    regexp_url = re.compile(r'.*\.iso')
    regexp_version = re.compile(r'download/(.*)/vyos')

    url_bases = [
        'https://vyos.net/get/nightly-builds/',
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, pattern=regexp_url):
            iso_size = get.size(iso_url)
            iso_arch = get.arch(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
