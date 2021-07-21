from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/debian-cd"
    subpaths = [
        "current-live/amd64/iso-hybrid",
        "current-live/i386/iso-hybrid",
        "current/amd64/iso-bd",
        "current/amd64/iso-cd",
        "current/amd64/iso-dvd",
        "current/arm64/iso-cd",
        "current/arm64/iso-dvd",
        "current/armel/iso-cd",
        "current/armel/iso-dvd",
        "current/i386/iso-bd",
        "current/i386/iso-cd",
        "current/i386/iso-dvd",
        "current/mips/iso-cd",
        "current/mips/iso-dvd",
        "current/mips64el/iso-cd",
        "current/mips64el/iso-dvd",
        "current/mipsel/iso-cd",
        "current/mipsel/iso-dvd",
        "current/multi-arch/iso-cd",
        "current/ppc64el/iso-cd",
        "current/ppc64el/iso-dvd",
        "current/s390x/iso-cd",
        "current/s390x/iso-dvd"
    ]

    for subpath in subpaths:

        path = f"{base_url}/{subpath}"
        html = bs(requests.get(path).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{path}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d+(.\d+(.\d+)?)?)", iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
