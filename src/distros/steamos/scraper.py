from public import *  # noqa


def init():

    array = []
    version_url = "https://steamcommunity.com/groups/steamuniverse/discussions/1"

    html = bs(requests.get(version_url).text, "html.parser")

    iso_url = "https://repo.steampowered.com/download/SteamOSDVD.iso"
    iso_arch = "amd64"
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"SteamOS update (\d+\.\d+) released", str(html)).group(1)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
