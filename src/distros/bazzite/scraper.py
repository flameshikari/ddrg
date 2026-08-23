from shared import *
from itertools import product

info = ns(
    name='Bazzite',
    url='https://bazzite.gg',
)

def get_urls():
    URLS = []
    BASE = 'https://download.bazzite.gg'
    HANDHELD = {'steamdeck','ally','legion','gpd','ayn','ayaneo','handheld','onexplayer','aokzoe','claw'}
    NO_GAMEMODE = {'nvidia','old-intel','surface','old-amd'}
    NO_PROP_NVIDIA = {'surface'}
    ASUS = {'asus'}
    DECK = HANDHELD | set()
    HARDWARE = ['desktop','htpc','framework-desktop','steamdeck','legion','ally','gpd','onexplayer',
                'aokzoe','ayn','ayaneo','claw','handheld','framework','laptop','asus-flow',
                'minisforum','virtualmachine','asus','surface']
    DE = ['kde','gnome','']
    GPU = ['amd','nvidia-open','intel','old-amd','nvidia','old-intel','']
    GM = ['yes','no','']
    def name_for(hw, de, gpu, gm):
        if hw == 'htpc':
            gm = 'yes'
        n = 'bazzite'
        if hw in DECK:
            n += '-deck'
        elif hw == 'asus' and gm == 'yes' and gpu != 'nvidia-open':
            n += '-ally'
        if gpu == 'nvidia-open' and gm == 'yes' and hw not in HANDHELD:
            n += '-nvidia'
        if de == 'gnome':
            n += '-gnome'
        if hw == 'asus' and gm != 'yes':
            n += '-asus'
        if hw == 'surface':
            n += '-surface'
        if gpu == 'nvidia' and hw not in HANDHELD and hw not in NO_PROP_NVIDIA:
            n += '-nvidia'
        if gpu == 'nvidia-open' and gm != 'yes' and hw not in HANDHELD:
            n += '-nvidia-open'
        if gpu == 'nvidia-open' and gm == 'yes':
            n = n.replace('bazzite', 'bazzite-deck', 1)
        elif gpu not in NO_GAMEMODE and hw not in NO_GAMEMODE and hw not in ASUS and gm == 'yes':
            n = n.replace('bazzite', 'bazzite-deck', 1)
        return n.replace('deck-deck', 'deck')
    names = sorted({name_for(*c) for c in product(HARDWARE, DE, GPU, GM)})
    for n in names:
        URLS.append(f'{BASE}/{n}-stable-amd64.iso')
        URLS.append(f'{BASE}/{n}-stable-live-amd64.iso')
    return URLS

@scraper
def init():
    values = []

    version = rq.get('https://api.github.com/repos/ublue-os/bazzite/releases').json()[0]['tag_name']
    
    arch = 'x86_64'

    for url, size in get.urls(get_urls()):
        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values