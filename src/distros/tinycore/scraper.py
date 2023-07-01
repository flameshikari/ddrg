from main import *  # noqa


def init():

    values = []

    url_version = 'http://tinycorelinux.net/downloads.html'
    response = str(rq.get(url_version).text)
    regexp_version_base = re.compile(r'Version (\d+).\d+')
    version_base = re.search(regexp_version_base, response).group(1)

    exceptions = ['current']

    url_bases = [
        f'http://tinycorelinux.net/{version_base}.x/x86/release/',
        f'http://tinycorelinux.net/{version_base}.x/x86_64/release/'
    ]

    regexp_version = re.compile(r'-(\d+\.\d+)\.')

    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions):

            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
