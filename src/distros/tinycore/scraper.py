from public import *  # noqa


def init():

    array = []
    version_url = "https://mirrors.dotsrc.org/tinycorelinux/welcome.html"
    base_urls = [
        "https://mirrors.dotsrc.org/tinycorelinux/{}.x/x86_64/release",
        "https://mirrors.dotsrc.org/tinycorelinux/{}.x/x86/release"
    ]

    html = bs(requests.get(version_url).text, "html.parser")
    version = re.search(r"latest version: <b>((\d+).\d+)", str(html))

    iso_version = version.group(1)
    base_version = version.group(2)

    for base_url in base_urls:

        base_url = base_url.format(base_version)
        html = bs(requests.get(base_url).text, "html.parser")

        for filename in html.find_all("a", {"href": re.compile("^.*\.iso$")}):

            iso_url = f"{base_url}/{filename['href']}"
            if "current" in iso_url: continue
            iso_arch = get_iso_arch(iso_url)
            iso_size = get_iso_size(iso_url)

            array.append((iso_url, iso_arch, iso_size, iso_version))

    return array
