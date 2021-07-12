from public import *  # noqa


base_url = "https://freedos.org/download/"


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for version in html.find_all("a"):
        version = version.get("href")
        if "/files/distributions/" in version:
            if version.endswith("/"):
                html = bs(requests.get(version)
                                  .text, "html.parser")
                for filename in html.find_all("a"):
                    filename = filename.get("href")
                    if filename.endswith(".iso"):
                        iso_url = version + filename
                        iso_arch = "i386"
                        iso_size = get_iso_size(iso_url)
                        iso_version = re.search(r"/(\d+.\d+)/", iso_url) \
                                        .group(1)
                        array.append((iso_url, iso_arch,
                                      iso_size, iso_version))
    return array
