from main import *  # noqa


def init():

    values = []
    url_base = "https://mirror.truenetwork.ru/deepin-cd/{}/"
    regexp_version = re.compile(r'/releases/(\d+([-\.a-zA-Z\d]+))/')
    url_version = 'https://www.deepin.org/en/download'
    iso_versions = sorted(list(map(lambda x: x[0],
                                             set(re.findall(regexp_version, str(rq.get(url_version).text)))
                         )))

    for iso_version in iso_versions:
        for iso_url in get.urls(url_base.format(iso_version)):
            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
