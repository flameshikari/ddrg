from public import *  # noqa


def init():

    array = []
    base_url = "https://slackware.uk/absolute"

    html = bs(requests.get(base_url).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = f"{base_url}/{filename['href']}"
        iso_arch = "x86_64" if "64" in iso_url else "i386"
        iso_size = get_iso_size(iso_url)
        iso_version = "15.0"

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
