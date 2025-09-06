from helpers import *

info = {
    'name': 'Devuan',
    'url': 'https://devuan.org'
}

def init():

    values = []
    exceptions = ['https://www.devuan.org', 'cd', 'CD'] + [f"_{str(i)}." for i in range(1, 4)]
    regexp_version = re.compile(r'_(\d+(\.\d+(\.\d+)?)?)')
    regexp_arm_version = re.compile(r'Installer/(\w+)/')
    url_bases = [
        'https://files.devuan.org/',
        'https://arm-files.devuan.org/Devuan-Arm64-Installer/'
    ]

    for iso_url in get.urls(url_bases[0], exclude=exceptions,
                                          recursive=True):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    for iso_url in get.urls(url_bases[1], exclude=exceptions,
                                          recursive=True):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_arm_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))




    return values
