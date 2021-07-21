from public import *  # noqa


def init():

    array = []
    base_url = "https://elementary.io/"

    html = bs(requests.get(base_url).text, "html.parser")

    iso_url = f"https:{html.find('a', {'class': 'http'})['href']}"
    iso_arch = "x86_64"
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"-(\d+(.\d+(.\d+)?)?)", iso_url).group(1)

    array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
