from shared import *

info = ns(
    name='PikaOS',
    url='https://pika-os.com',
)

def get_release():
    fallback = '4.0-amd64-v3-26.08.20-4'

    # The public wiki is not behind the challenge used by the main website.
    # Its home-page update date tracks the ISO links published on pika-os.com.
    wiki = rq.get('https://wiki.pika-os.com/en/home').text
    match = re.search(r'updated-at="(\d{4})-(\d{2})-(\d{2})T', wiki)
    if not match:
        return fallback

    year, month, day = match.groups()
    date = f'{year[2:]}.{month}.{day}'
    if date in fallback:
        return fallback

    current_major = int(fallback.split('.', 1)[0])
    majors = [current_major] + [major for major in range(1, 11) if major != current_major]
    for major in majors:
        for revision in range(1, 11):
            release = f'{major}.0-amd64-v3-{date}-{revision}'
            probe = f'https://iso.pika-os.com/PikaOS-Nest-GNOME-{release}.iso'
            if rq.head(probe, allow_redirects=True).status_code == 200:
                return release

    return fallback

@scraper
def init():
    values = []

    regexp = r'-(\d+\.\d+(?:\.\d+)?)'

    base = 'https://iso.pika-os.com'
    release = get_release()
    editions = ['GNOME', 'KDE', 'Hyprland', 'Niri', 'COSMIC']
    targets = [
        f'{base}/PikaOS-Nest-{variant}{edition}-{release}.iso'
        for edition in editions
        for variant in ['', 'NVIDIA-']
    ]
    
    for url, size in get.urls(targets):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values
