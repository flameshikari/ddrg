from public import *  # noqa


base_url = "https://endeavouros.com/latest-release/"


def init():
    array = []
    html = str(bs(requests.get(base_url).text, "html.parser"))
    filename = re.search(r'<strong>(endeavouros.*.iso)</strong>', html) \
                 .group(1)
    iso_url = "https://github.com/endeavouros-team/ISO/releases/" \
              "download/1-EndeavourOS-ISO-releases-archive/" + filename
    iso_arch = get_iso_arch(iso_url)
    iso_size = get_iso_size(iso_url)
    iso_version = re.search(r"-(\d{4}.\d{2}.\d{2})", iso_url).group(1)
    array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
