from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'Current release: V(\d+(\.\d+(\.\d+)?)?)')
    url_base = 'https://mirror.clientvps.com/ubcd/'
    url_version = 'https://www.ultimatebootcd.com/download.html'
    response = rq.get(url_version)

    iso_version = re.search(regexp_version, str(response.text)).group(1)
    iso_url = f'{url_base}ubcd{iso_version.replace(".", "")}.iso'
    iso_arch = 'bios'
    iso_size = get.size(iso_url)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
