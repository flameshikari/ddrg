from shared import *

info = ns(
    name='PikaOS',
    url='https://pika-os.com',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'

    target = 'https://git.pika-os.com/website/site/raw/commit/849bb5c9a57bd79bbc5d08b6b3c27f3b47a013f5/src/lib/content/wiki.json'
    
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
