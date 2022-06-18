from main import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'-(\d+\.\d+(\.\d+)?)-')
    url_base = 'https://api.github.com/repos/ChimeraOS/install-media/releases/latest'

    iso_url = json.loads(rq.get(url_base).text)['assets'][0]['browser_download_url']
    iso_arch = get.arch(iso_url)
    iso_size = get.size(iso_url)
    iso_version = re.search(regexp_version, iso_url).group(1)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
