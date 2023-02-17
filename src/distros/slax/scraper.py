from main import *  # noqa


def init():

    values = []

    url_bases = [
        'https://ftp.linux.cz/pub/linux/slax/Slax-11.x/',
        'https://ftp.linux.cz/pub/linux/slax/Slax-15.x/'
    ]

    regexp_version = re.compile(r'-(\d+(\.\d+(\.\d+)?)?)')

    for url_base in url_bases:

        for iso_url in get.urls(url_base):

            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
