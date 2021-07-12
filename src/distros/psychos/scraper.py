from public import *  # noqa


base_url = "https://psychoslinux.gitlab.io/downloads.html"


def init():
    array = []
    html = bs(requests.get(base_url).text, "html.parser")
    for link in html.find_all("a"):
        link = link.get("href")
        try:
            if link.endswith(".iso"):
                iso_url = link
                iso_arch = "i486" if "486" in iso_url else "i686"
                iso_size = get_iso_size(iso_url)
                iso_version = re.search(r"(\d+.\d+.\d+).iso", iso_url) \
                                .group(1)
                array.append((iso_url, iso_arch, iso_size, iso_version))
        except:
            continue
    return array
