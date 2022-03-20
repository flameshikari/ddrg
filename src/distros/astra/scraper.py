from public import *  # noqa


def init():

    array = []
    base_url = "https://mirror.yandex.ru/astra/stable/orel/iso"

    html = bs(requests.get(base_url).text, "html.parser")

    for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

        iso_url = f"{base_url}/{filename['href']}"
        skip_these = ["current", "stable"]
        if any(x in filename['href'] for x in skip_these): continue

        iso_arch = "x86_64"
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"orel-(\d+.\d+.\d+(\.\d+)?)", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
