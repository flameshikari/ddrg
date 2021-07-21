from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/ubuntu-cdimage/xubuntu/releases"

    html = bs(requests.get(base_url).text, "html.parser")

    for version in html.find_all("a", {"href": re.compile("^[a-z].*/$")}):

        path = f"{base_url}/{version['href'][:-1]}/release"
        html = bs(requests.get(path).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+.\d+(.\d+)?)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
