from main import *  # noqa


def init():

    values = []
    exceptions = [
        'tools', 'unofficial', 'pre-', 'previews',
        'repos', 'fdbasews', 'fbasecd'
        ]
    regexp_url = re.compile(r'.*\d+\.\d+.*')
    regexp_version = re.compile(r'.*\/(\d+\.\d+)\/.*')
    url_base = "https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/"

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      pattern=regexp_url,
                                      recurse=True):
        iso_arch = "i386"
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
