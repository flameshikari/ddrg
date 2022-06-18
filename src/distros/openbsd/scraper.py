from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'OpenBSD/(\d+\.\d+)/')
    url_base = 'https://www.openbsd.org/faq/faq4.html'

    for iso_url in get.urls(url_base):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
