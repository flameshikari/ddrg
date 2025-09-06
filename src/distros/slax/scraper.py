from helpers import *

info = {
    'name': 'Slax',
    'url': 'https://slax.org'
}

def init():

    values = []

    url_base = 'https://ftp.cvut.cz/mirrors/slax/'
    excludes = ['Slax-old', 'Slax-Debian', 'Slax-Slackware', 'source']
    regexp_version = re.compile(r'-(\d+(\.\d+(\.\d+)?)?)')

    for iso_url in get.urls(url_base, exclude=excludes, pattern='Slax-', recursive=True):

        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
