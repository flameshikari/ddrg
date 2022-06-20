from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+).iso')
    url_base = 'https://iso.builds.garudalinux.org/iso/latest/garuda/'

    for iso_url in get.urls(url_base, recurse=True):

        iso_url = rq.get(iso_url, allow_redirects=False).headers['Location']
        iso_arch = "amd64"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)

        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
