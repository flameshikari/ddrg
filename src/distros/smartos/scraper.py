from helpers import *

info = {
    'name': 'SmartOS',
    'url': 'https://www.tritondatacenter.com/smartos'
}

def get_urls(url):
    response = rq.get(url + '?limit=1024', stream=True)
    response.raise_for_status()
    timestamp_pattern = re.compile(r'^\d{8}T\d{6}Z$')
    names = []
    for line in response.iter_lines():
        if line:
            obj = json.loads(line)
            name = obj.get('name')
            if name and timestamp_pattern.match(name):
                names.append(f"{url}/{name}/smartos-{name}.iso")
    names.sort(reverse=True)
    return names[:20]

def init():

    values = []
    regexp_version = re.compile(r'-(\d+T\d+Z)\.iso')
    url_base = 'https://us-central.manta.mnx.io/Joyent_Dev/public/SmartOS'

    for iso_url in get_urls(url_base):
        iso_url = get.urls(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
