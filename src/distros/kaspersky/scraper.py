from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
    url_base = 'https://support.kaspersky.ru/utility'
    iso_url = get.urls(url_base)[0]
    url_version = 'https://support.kaspersky.ru/krd' + re.search(r'\/20(\d+)\/', iso_url).group(1) + '/new/'
    iso_version = re.search(regexp_version, str(rq.get(url_version).text)).group()
    iso_arch = get.arch(iso_url)
    iso_size = get.size(iso_url)
        
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
