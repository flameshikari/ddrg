from main import *  # noqa


def init():

    values = []
    regexp_url = re.compile(r'.*-iso/.*')
    regexp_version = re.compile(r'-(\d+\.\d+)-')
    url_base = 'https://slackware.uk/slackware/slackware-iso/'

    for iso_url in get.urls(url_base, pattern=regexp_url,
                                      recurse=True):
        iso_arch = "x86_64" if "64" in iso_url else "i386"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
