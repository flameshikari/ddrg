from public import *  # noqa


def init():

    array = []
    base_url = "https://q4os.org/redirect1{}.html"

    for number in range(0, 4):

        html = bs(requests.get(base_url.format(number)).text, "html.parser")
        regex = re.compile("^.*\.iso/download$")
        
        iso_url = html.find_all("a", {"href": regex})[0]["href"][:-9]
        iso_arch = get_iso_arch(iso_url)
        iso_size = get_iso_size(iso_url)
        iso_version = re.search(r"-(\d+\.\d+)", iso_url).group(1)

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
