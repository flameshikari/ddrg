from shared import *

info = ns(
    name='Bazzite',
    url='https://bazzite.gg',
)

def get_urls():
    workflow = rq.get(
        'https://raw.githubusercontent.com/ublue-os/bazzite/'
        'main/.github/workflows/build_iso.yml'
    )
    workflow.raise_for_status()
    matrix = yaml.safe_load(workflow.text)
    images = matrix['jobs']['build-iso']['strategy']['matrix']['image_name']

    return [
        f'https://download.bazzite.gg/{image}-stable-live-amd64.iso'
        for image in images
    ]

@scraper
def init():
    values = []

    version = rq.get(
        'https://api.github.com/repos/ublue-os/bazzite/releases/latest'
    ).json()['tag_name']
    
    arch = 'x86_64'

    for url, size in get.urls(get_urls()):
        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
