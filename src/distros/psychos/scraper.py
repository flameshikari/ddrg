from public import *  # noqa


def init():

    array = []
    base_url = "https://psychoslinux.gitlab.io/downloads.html"

    html = bs(requests.get(base_url).text, "html.parser")

    for target in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = target["href"]
        iso_arch = "i486" if "486" in iso_url else "i686"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"(\d+.\d+.\d+).iso", iso_url).group(1)
        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
