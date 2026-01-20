from shared import *

info = ns(
    name='SteamOS',
    url='https://store.steampowered.com/steamos',
)

@scraper
def init():
    values = []

    regexp = re.compile(r'-(\d+\.\d+(\.\d+)?)_')
    
    target = 'stash:steamos'

    for url, size in get.urls(target):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values