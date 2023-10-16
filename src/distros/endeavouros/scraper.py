from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'[-_](\d+[-_]\d+(_R\d+)?)')
    url_base = 'https://mirror.moson.org/endeavouros/iso/'

    for iso_url in get.urls(url_base):

        iso_arch = "x86_64"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1).replace('-', '_')
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
