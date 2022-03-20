from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/mirrors/deepin/releases"

    html = bs(requests.get(base_url).text, "html.parser")

    tmp = html.find_all("a", {"href": re.compile("^.*/$")})
    versions = [tmp[-1]["href"][:-1], tmp[-2]["href"][:-1]]

    for iso_version in versions:

        html = bs(requests.get(f"{base_url}/{iso_version}").text, "html.parser")
        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{base_url}/{iso_version}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
