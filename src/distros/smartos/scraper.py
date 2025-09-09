from shared import *

info = ns(
    name='SmartOS',
    url='https://tritondatacenter.com/smartos',
)

def get_urls(url):
    response = rq.get(url + '?limit=1024', stream=True)
    pattern = re.compile(r'^\d{8}T\d{6}Z$')
    names = []
    for line in response.iter_lines():
        if line:
            obj = json.loads(line)
            name = obj.get('name')
            if name and pattern.match(name):
                names.append(f"{url}/{name}/smartos-{name}.iso")
    names.sort(reverse=True)
    return names[:20]

@scraper
def init():
    values = []

    regexp = r'-(\d+T\d+Z)\.iso'

    target = get_urls('https://us-central.manta.mnx.io/Joyent_Dev/public/SmartOS')

    for url, size in get.urls(target):

        arch = 'x86_64'
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values