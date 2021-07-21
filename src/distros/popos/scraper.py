from public import *  # noqa


def init():

    array = []
    base_urls = [
        "https://api.pop-os.org/builds/20.04/intel",
        "https://api.pop-os.org/builds/21.04/intel",
        "https://api.pop-os.org/builds/20.04/nvidia",
        "https://api.pop-os.org/builds/21.04/nvidia"
    ]

    for base_url in base_urls:

        response = json.loads(requests.get(base_url).text)

        iso_url = response["url"]
        iso_arch = "amd64"
        iso_size = response["size"]
        iso_version = response["version"]

        array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
