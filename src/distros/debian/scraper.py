from public import *  # noqa


def init():

    values = []
    exceptions = ['bt', 'jigdo', 'list', 'log', 'source']
    regexp_version = re.compile(r'-(\d+\.\d+(\.\d+)?)')
    url_bases = [
        'https://mirror.yandex.ru/debian-cd/current/',
        'https://mirror.yandex.ru/debian-cd/current-live/' ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions,
                                          recurse=True):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
