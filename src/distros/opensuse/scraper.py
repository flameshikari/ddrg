from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+(\.\d+)?)')
    url_bases = [
        'https://software.opensuse.org/distributions/tumbleweed',
        'https://software.opensuse.org/distributions/leap'
    ]
    for url_base in url_bases:
        for iso_url in get.urls(url_base):

            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = 'Leap ' + re.search(regexp_version, iso_url).group(1) \
                if 'tumbleweed' not in iso_url else 'Tumbleweed'
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
