from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+[.-]\d+\.\d+)')
    exceptions = [
        'Container', 'Cloud', 'os',
        'images', 'source', 'Spins', 'Modular'
    ]
    url_bases = [
        'https://mirror.yandex.ru/fedora/linux/releases/35/',
        'https://mirror.yandex.ru/fedora/linux/releases/test/36_Beta/'
    ]

    url_bases = [
        'https://fedoraproject.org/workstation/download/',
        'https://fedoraproject.org/server/download/',
        'https://fedoraproject.org/iot/download/',
        'https://fedoraproject.org/coreos/download/',
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    # for url_base in url_bases:
    #     for iso_url in get.urls(url_base, exclude=exceptions,
    #                                       recurse=True):
    #         iso_arch = get.arch(iso_url)
    #         iso_size = get.size(iso_url)
    #         iso_version = re.search(regexp_version, iso_url).group(1)
    #         values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
