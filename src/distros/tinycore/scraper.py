from public import *  # noqa


homepage = "https://mirrors.dotsrc.org/tinycorelinux/welcome.html"

base_urls = [
    "https://mirrors.dotsrc.org/tinycorelinux/{}.x/x86_64/release/",
    "https://mirrors.dotsrc.org/tinycorelinux/{}.x/x86/release/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(homepage).text, "html.parser")
        target = html.find_all("p")[6]
        version = re.findall(r"(\d+)\.\d+", str(target))[0]
        base_url = base_url.format(version)
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith(".iso"):
                iso_url = base_url + filename
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                try:
                    iso_version = re.search(r"-(\d+\.\d+)\.iso", iso_url) \
                                    .group(1)
                except:
                    continue
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
