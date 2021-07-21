from public import *  # noqa


def init():

    array = []
    base_urls = [
        "https://sourceforge.net/projects/clonezilla/rss?path=/clonezilla_live_stable/{}",
        "https://sourceforge.net/projects/clonezilla/rss?path=/clonezilla_live_alternative/{}"
    ]
    version_urls = [
        "https://clonezilla.org/downloads/download.php?branch=stable",
        "https://clonezilla.org/downloads/download.php?branch=alternative"
    ]

    for i in [0, 1]:

        html = bs(requests.get(version_urls[i]).text, "html.parser")
        version = re.search(r'Clonezilla live version: <font color="red">(.*)</font>', str(html)).group(1)

        xml = bs(requests.get(base_urls[i].format(version)).text, "xml")

        for item in xml.find_all("item"):
            content = item.find("content")
            iso_url = content["url"][:-9]

            if iso_url.endswith(".iso"):

                iso_arch = get_iso_arch(iso_url)
                iso_size = int(content["filesize"])
                iso_version = re.search(r"-(\d+.\d+.\d+-\d+)", iso_url).group(1) \
                    if "stable" in iso_url \
                    else re.search(r"-(\d{8})", iso_url).group(1)

                array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
