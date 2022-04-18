from public import *  # noqa


def init():

    values = []
    regexp_url = re.compile(r'\/\/.*\.iso')
    regexp_version = re.compile(r'-(\d+(.\d+(.\d+)?)?)')
    url_base = 'https://elementary.io/'

    for iso_url in get.urls(url_base, add_base=False,
                                      pattern=regexp_url):
        iso_url = 'http:' + iso_url
        iso_arch = "x86_64"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
