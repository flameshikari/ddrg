from public import *  # noqa


def init():

    array = []
    versions = []
    version_url = "https://linuxmint.com/download_all.php"
    base_url = "https://mirror.yandex.ru/linuxmint/stable"

    html = bs(requests.get(version_url).text, "html.parser")
    regex = re.compile("release.php")

    for version in html.find_all("a", {"href": regex}):
        if version.text[0].isdigit():
            versions.append(version.text)

    for iso_version in versions:

        path = f"{base_url}/{iso_version}"
        html = bs(requests.get(path).text, "html.parser")
        regex = re.compile("^.*\.iso$")

        for filename in html.find_all("a", {"href": regex}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
