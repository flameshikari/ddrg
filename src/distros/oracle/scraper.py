from main import *  # noqa


def init():

    values = []
    exceptions = ['uek', 'src']
    regexp_version = re.compile(r'/(OL\d+/u\d+)/')
    url_base = 'https://yum.oracle.com/oracle-linux-isos.html'

    for iso_url in get.urls(url_base, exclude=exceptions):

        iso_url = iso_url.replace('oracle-linux-isos.html', '')
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = '.'.join(re.sub(r'[OLu]', '', re.search(regexp_version, iso_url).group(1)).split('/'))
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values