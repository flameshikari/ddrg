from shared import *

info = ns(
    name='Peppermint OS',
    url='https://peppermintos.com',
)

# def get_version():
#     target = 'https://sourceforge.net/p/peppermintos/pepwiki/BuildDate/'
#     regexp = re.compile(r'Build Date: (\d+-\d+-\d+) ')
#     response = str(rq.get(target).text)
#     print(response)
#     return re.search(regexp, response).group(1)

@scraper
def init():
    values = []

    target = 'https://sourceforge.net/projects/peppermintos/files/isos/'
    
    # version = get_version()

    for url, size in get.urls(target):

        arch = get.arch(url)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version='',
        ))

    return values
