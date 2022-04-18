from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'You should download antiX-(\d+(\.\d+(\.\d+)?)?)')
    url_base = 'https://mirror.yandex.ru/mirrors/MX-Linux/MX-ISOs/ANTIX/Final/antiX-{}/'
    url_version = 'https://antixlinux.com/download/'
    response = rq.get(url_version)
    iso_version = re.search(regexp_version, str(response.text)).group(1)

    for iso_url in get.urls(url_base.format(iso_version)):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
