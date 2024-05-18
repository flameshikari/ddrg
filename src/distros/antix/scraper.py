from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'antiX-(\d+(\.\d+(\.\d+)?)?) files')
    url_base = 'https://antixlinux.com/download/'
    url_version = 'https://antixlinux.com/download/'
    response = rq.get(url_version)
    iso_version = re.search(regexp_version, str(response.text)).group(1)

    for iso_url in get.urls(url_base.format(iso_version)):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
