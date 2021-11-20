from public import *  # noqa


def init():

    array = []

    base_url = "https://ant.seedhost.eu/arcolinux/iso/"
    
    html = bs(requests.get(base_url).text, "html.parser")
    version = html.find_all("tr")[-1].a.get_text()[1:]
    
    html = bs(requests.get(f"{base_url}v{version}/").text, "html.parser")
    regex = re.compile("^.*\.iso$")

    for target in html.find_all("a", {"class": "name", "href": regex}):
        try:
            iso_url = f"{base_url}v{version}/{target['href']}"
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)
            iso_version = re.search(r"-v(\d+(.\d+(.\d+)?)?)", iso_url).group(1)
            array.append((iso_url, iso_arch, iso_size, iso_version))
        except:
            pass
    
    return array
