from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'Linux Lite (\d+(\.\d+)?)')
    url_version = 'https://www.linuxliteos.com/download.php'
    response = rq.get(url_version)
    iso_version = re.search(regexp_version, str(response.text)).group(1)
    url_base = f'http://repo.linuxliteos.com/linuxlite/isos/{iso_version}/'

    for iso_url in get.urls(url_base):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
