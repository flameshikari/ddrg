from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'(\d+.\d+.\d+).iso')
    url_base = 'https://psychoslinux.gitlab.io/downloads.html'

    for iso_url in get.urls(url_base):

        iso_arch = 'i486' if '486' in iso_url else 'i686'
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
