from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+(\.\d+)?)')
    exceptions = ['current']
    url_bases = [
        'https://mirrors.dotsrc.org/tinycorelinux/13.x/x86_64/release/',
        'https://mirrors.dotsrc.org/tinycorelinux/13.x/x86/release/'
    ]
    
    for url_base in url_bases:
        for iso_url in get.urls(url_base, exclude=exceptions):

            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)
            iso_version = re.search(regexp_version, iso_url).group(1)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
