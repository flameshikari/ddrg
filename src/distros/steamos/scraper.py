from public import *  # noqa


def init():

    values = []
    regexp_version = re.compile(r'SteamOS update (\d+\.\d+) released')
    url_version = 'https://steamcommunity.com/groups/steamuniverse/discussions/1'
    response = rq.get(url_version)

    iso_version = re.search(regexp_version, str(response.text)).group(1)
    iso_url = 'https://repo.steampowered.com/download/SteamOSDVD.iso'
    iso_arch = 'amd64'
    iso_size = get.size(iso_url)
    values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
