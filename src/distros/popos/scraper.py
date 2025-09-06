from helpers import *

info = {
    'name': 'Pop!_OS',
    'url': 'https://pop.system76.com'
}

def init():

    values = []
    url_base = 'https://api.pop-os.org/builds/{}/{}'
    iso_versions = ['24.04', '22.04']
    arch_versions = ['intel', 'nvidia']
    regexp_version = re.compile(r'_(\d+.\d+)_')

    for iso_version in iso_versions:
        for arch_version in arch_versions:
            try:
                iso_url = get.urls(url_base.format(iso_version, arch_version), json=True)[0]
                iso_arch = get.arch(iso_url)
                iso_size = get.size(iso_url)
                iso_version = re.search(regexp_version, iso_url).group(1)

                values.append((iso_url, iso_arch, iso_size, iso_version))
            except:
                continue
    
    return values
