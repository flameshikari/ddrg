from main import *  # noqa


def init():

    values = []

    url_base = 'https://sourceforge.net/projects/nitruxos/files/Release/ISO/'
    url_version = 'https://nxos.org/'

    regexp_version = re.compile(r'Nitrux (\d+\.\d+\.\d+)')
    iso_version = re.search(regexp_version,
                            str(rq.get(url_version).text)).group(1)

    for iso_url in get.urls(url_base):

        iso_size = iso_url['size']
        iso_url = iso_url['url']
        iso_arch = get.arch(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values