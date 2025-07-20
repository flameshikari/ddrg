from main import *  # noqa
import yaml


def build(name):
    base = f'https://raw.githubusercontent.com/ublue-os/bazzite/refs/heads/main/.github/workflows/{name}.yml'
    return yaml.safe_load(rq.get(base).text)['jobs']['build-iso']['strategy']['matrix']['image_name']


def init():

    values = []
    base_url = 'https://download.bazzite.gg'

    iso_version = rq.get('https://api.github.com/repos/ublue-os/bazzite/releases').json()[0]['tag_name']

    iso_arch = 'x86_64'

    images = build('build_iso')
    images_live = build('build_iso_titanoboa')

    for image in images:
        iso_url = f'{base_url}/{image}-stable-amd64.iso'
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    for image in images_live:
        iso_url = f'{base_url}/{image}-stable-live.iso'
        iso_size = get.size(iso_url)
        values.append((iso_url, iso_arch, iso_size, 'Live'))

    return values
