from public import *  # noqa


def init():

    array = []
    base_urls = [
        "https://mirror.truenetwork.ru/kali-images/current/",
        "https://mirror.truenetwork.ru/kali-images/kali-weekly/"
    ]

    for base_url in base_urls:

        html = bs(requests.get(base_url).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{base_url}/{filename['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-(\d{4}.[A-Z0-9]+)-",iso_url).group(1)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
