from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'\(v(\d+(.\d+(.\d+)?)?)\)')
    url_version = 'https://www.hirensbootcd.org/download/'
    response = rq.get(url_version)

    iso_version = re.search(regexp_version, str(response.text)).group(1)
    iso_url = 'https://www.hirensbootcd.org/files/HBCD_PE_x64.iso'
    iso_arch = get.arch(iso_url)
    iso_size = get.size(iso_url)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
