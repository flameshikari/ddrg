from helpers import *

info = {
    'name': 'OpenSUSE',
    'url': 'https://opensuse.org'
}

def init():

    url_version = 'https://get.opensuse.org/'
    response = str(rq.get(url_version).text)

    version_leap = re.search(re.compile(r'Leap (\d+(\.\d+)?)'), response).group(1)
    version_leap_micro = re.search(re.compile(r'Leap Micro (\d+(\.\d+)?)'), response).group(1)

    url_bases = [
        'https://get.opensuse.org/tumbleweed',
        f'https://get.opensuse.org/leapmicro/{version_leap_micro}/',
        f'https://get.opensuse.org/leap/{version_leap}/'
    ]

    values = []
    regexp_version = re.compile(r'/(\d+(\.\d+)?)/')

    for url_base in url_bases:
        for iso_url in get.urls(url_base):

            iso_arch = get.arch(iso_url)
            iso_size = get.size(iso_url)

            try:
                version = re.search(regexp_version, iso_url).group(1)
                if '/leap-micro/' in iso_url:
                    iso_version = 'Leap Micro ' + version
                elif '/leap/' in iso_url:
                    iso_version = 'Leap ' + version
            except:
                iso_version = 'Tumbleweed'

            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
