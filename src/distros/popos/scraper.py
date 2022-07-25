from main import *  # noqa


def init():

    values = []
    url_bases = [
        'https://api.pop-os.org/builds/22.04/intel',
        'https://api.pop-os.org/builds/21.10/intel',
        'https://api.pop-os.org/builds/20.04/intel',
        'https://api.pop-os.org/builds/22.04/nvidia',
        'https://api.pop-os.org/builds/21.10/nvidia',
        'https://api.pop-os.org/builds/20.04/nvidia'
    ]

    for url_base in url_bases:

        response = json.loads(rq.get(url_base).text)
        iso_url = response['url']
        iso_arch = 'amd64'
        iso_size = response['size']
        iso_version = response['version']
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
