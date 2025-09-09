from shared import *

info = ns(
    name='Bazzite',
    url='https://bazzite.gg',
)

def get_urls():
    base_url = 'https://download.bazzite.gg'
    target_url = 'https://github.com/ublue-os/bazzite/raw/main/.github/workflows/{0}.yml'
    filenames = ['build_iso', 'build_iso_titanoboa']
    urls = []
    for filename in filenames:
        url = target_url.format(filename)
        parsed = yaml.safe_load(rq.get(url).text)
        image_names = parsed['jobs']['build-iso']['strategy']['matrix']['image_name']
        for image_name in image_names:
            url = f'{base_url}/{image_name}'
            if 'titanoboa' in filename: url += '-stable-live.iso'
            else: url += '-stable-amd64.iso'
            urls.append(url)
    return urls

@scraper
def init():
    values = []

    version = rq.get('https://api.github.com/repos/ublue-os/bazzite/releases').json()[0]['tag_name']
    
    arch = 'x86_64'

    for url, size in get.urls(get_urls()):

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values