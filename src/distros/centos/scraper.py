from main import *  # noqa


def init():

    values = []
    exceptions = ['latest', 'source', '/os/']
    regexp_version = re.compile(r'-(\d+(-\d+)?)')
    url_bases = [
        'https://mirror.truenetwork.ru/centos-altarch/7/isos/',
        'https://mirror.truenetwork.ru/centos/8-stream/isos/',
        'https://mirror.truenetwork.ru/centos-stream/9-stream/BaseOS/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions,
                                          recurse=True):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1).replace('-', ' ')
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
