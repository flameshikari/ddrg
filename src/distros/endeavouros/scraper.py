from public import *  # noqa


def init():

    array = []
    base_url = "https://endeavouros.com/latest-release"

    html = bs(requests.get(base_url).text, "html.parser")
    
    for filename in html.find_all("a", {"href": re.compile("^.*github.com.*\.iso$")}):

        iso_url = filename['href']
        iso_arch = "x86_64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d+(_\d+)?)", iso_url).group(1).replace('_', '.')

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
