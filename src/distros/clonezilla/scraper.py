from helpers import *

info = {
    'name': 'Clonezilla',
    'url': 'https://clonezilla.org'
}

def init():

    values = []
    branches = ['alternative', 'stable']
    regexp_version = re.compile(r'Clonezilla live version: <font color=.?red.?>(.*)<\/font>')
    url_base = 'https://sourceforge.net/projects/clonezilla/files/clonezilla_live_{}/{}/'
    url_version = 'https://clonezilla.org/downloads/download.php?branch={}'

    for branch in branches:
        response = rq.get(url_version.format(branch))
        iso_version = re.search(regexp_version, str(response.text)).group(1)

        try:
            iso_urls = get.urls(url_base.format(branch, iso_version))
        except:
            continue

        for iso_url in iso_urls:
            iso_size = iso_url['size']
            iso_url = iso_url['url']
            iso_arch = get.arch(iso_url)
            values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
