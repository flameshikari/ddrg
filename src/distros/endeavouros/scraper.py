from public import *  # noqa


def init():

    values = []
    regexp_url = re.compile(r'.*github.com.*.iso')
    regexp_version = re.compile(r'_(\d+(_\d+)?)')
    url_base = 'https://endeavouros.com/latest-release/'

    for iso_url in get.urls(url_base, pattern=regexp_url):

        iso_arch = "x86_64"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1).replace('_', '.')
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
