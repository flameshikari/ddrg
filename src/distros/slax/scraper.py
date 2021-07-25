from public import *  # noqa


def init():

    array = []
    base_url = "https://www.slax.org"

    html = bs(requests.get(base_url).text, "html.parser")
    iso_version = re.search(r"-(\d+(.\d+(.\d+)?)?).iso", str(html)).group(1)

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = filename["href"]
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array