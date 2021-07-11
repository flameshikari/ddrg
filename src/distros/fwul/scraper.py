from public import *  # noqa


base_url = "https://androidfilehost.com/?fid=8889791610682936459"


def init():
    iso_url = get_afh_url(base_url)
    iso_arch = get_iso_arch(iso_url)
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"v(\d+.\d+)", iso_url).group(1)
    return [(iso_url, iso_arch, iso_size, iso_version)]
