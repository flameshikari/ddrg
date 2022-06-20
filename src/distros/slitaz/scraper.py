from main import *  # noqa


def init():

    values = []

    url_version = "https://www.slitaz.org/en/"
    regexp_version = re.compile(r'SliTaz (\d+(.\d+)?) Rolling')
    iso_version = re.search(regexp_version,
                            str(rq.get(url_version).text)).group(1)
    url_base = 'https://mirror.slitaz.org/iso/latest/'

    for iso_url in get.urls(url_base):
        
        iso_size = get.size(iso_url)
        if any(x in iso_url for x in ["rolling.iso", "loram.iso"]): iso_arch = "i386"
        else: iso_arch = "x86_64"

        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
