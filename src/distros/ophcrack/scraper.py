from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(\.\d+)?)\.iso')
    url_base = 'https://sourceforge.net/projects/ophcrack/files/ophcrack-livecd/3.6.0/'

    for iso_url in get.urls(url_base):

        iso_arch = 'x86_64'
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
