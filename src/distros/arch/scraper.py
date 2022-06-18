from main import *  # noqa


def init():

    values = []
    exceptions = ['arch/', 'latest/']
    regexp_version = re.compile(r'-(\d+.\d+(.\d+)?)')
    url_base = 'https://mirror.yandex.ru/archlinux/iso/'

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      recurse = True):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        try: iso_version = re.search(regexp_version, iso_url).group(1)
        except: continue
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
