from public import *  # noqa


def init():

    values = []
    exceptions = ['boot.iso', 'latest']
    regexp_version = re.compile(r'-(\d+(.\d+(.\d+)?)?)')
    url_bases = [
        'http://mirror.truenetwork.ru/centos/8-stream/isos/',
        'http://mirror.truenetwork.ru/centos-stream/9-stream/BaseOS/',
        'http://mirror.truenetwork.ru/centos/7.9.2009/isos/',
        'http://mirror.truenetwork.ru/centos-altarch/7.9.2009/isos/'
    ]

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions,
                                          recurse=True):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
