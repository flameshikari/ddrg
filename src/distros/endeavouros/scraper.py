from main import *  # noqa
from datetime import datetime


def init():

    values = []
    regexp_version = re.compile(r'[-|_](\d+\.\d+\.\d+|\d+_\d+|\d+-\d+)')
    url_base = 'http://md.mirrors.hacktegic.com/endeavouros/iso/'

    for iso_url in get.urls(url_base):
        iso_arch = "x86_64"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1).replace('-', '.').replace('_', '.')
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
