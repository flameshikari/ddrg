from helpers import *

info = {
    'name': 'Android-x86',
    'url': 'https://android-x86.org'
}

def init():

    values = []
    regexp_version = re.compile(r'-v?(\d+(\.\d+)?)')
    exceptions = ['/Testing/']
    url_base = 'https://sourceforge.net/projects/android-x86/files/'

    for iso_url in get.urls(url_base, recursive=True, exclude=exceptions):

        iso_size = iso_url['size']
        iso_url = iso_url['url']            
        iso_arch = get.arch(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
