from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile('<a href=\'./v(.*?)\'')
    url_base = 'https://ant.seedhost.eu/arcolinux/iso/'
    response = rq.get(url_base)
    iso_version = re.findall(regexp_version, str(response.text))[-1]

    for iso_url in get.urls(f'{url_base}v{iso_version}/'):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
