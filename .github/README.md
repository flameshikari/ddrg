<br>
<p align="center">
  <img src="./src/website/root/assets/logo.svg" width="250" alt="">
</p>
  <h1 align="center">
    <a href="https://www.drivedroid.io/">DriveDroid</a> Repository Generator <img src="https://github.com/flameshikari/ddrg/actions/workflows/builder.yml/badge.svg">
  </h1>
</p>

## 🚧 Disclaimer

This tool in under continuous development, but it kinda works. Beware a lot of weird code!

## 💿 Try It Now

Just add the following link to the image repositories in DriveDroid:
```
https://dd.hexed.pw/repo.json
```

## 🐍 Installation

### Requirements

`Python 3.8+` with package `venv`. If `venv` is missing, try to search for `python-venv` via your system package manager and install it, else [search on Google](https://www.google.com/search?q=python+install+venv) how to install it in your system.

### Virtual Environment

Follow next commands to setup the repository generator:

```bash
# create the virtual environment
python -m venv env

# activate the virtual environment
source env/bin/activate

# install required packages
pip install -r requirements.txt
```


## 📝 Writing Scrapers

Create a folder in **[distros](../tree/master/src/distros)** with the next structure:

```
distro_name
├── logo.png
└── scraper.py
```

If `distro_name` starts with the underscore (e.g. **_disabled**), it will be excluded from scraping.

### `logo.png`

Should be 128x128px with transparent background. Arch Linux **[logo.png](../raw/master/src/distros/arch/logo.png)** example:

<br><p align="center">
  <img src="../raw/master/src/distros/arch/logo.png" alt="Arch Linux"/>
</p><br>

### `scraper.py`

A scraper can be written as you like, as long as it returns the desired values: the array of tuples (every tuple contains **iso_url**, **iso_arch**, **iso_size**, **iso_version** in order) and contains `info` variable with the name and the homepage url of the distro (see the example below).

`from helpers import * ` at the top of a scraper includes helpful functions and classes from `helpers.py`.

For example, **[Arch Linux](../raw/master/src/distros/arch/scraper.py)** scraper looks like this:

```python
from helpers import *

info = {
    'name': 'Arch Linux',
    'url': 'https://archlinux.org'
}

def init():

    values = []
    exceptions = ['arch/', 'latest/', 'archlinux-x86_64']
    regexp_version = re.compile(r'-(\d+.\d+(.\d+)?)')
    url_base = 'https://mirror.yandex.ru/archlinux/iso/'

    for iso_url in get.urls(url_base, exclude=exceptions,
                                      recursive=True):
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values

```

This scraper returns values similar to the following:

```python
[
  (
    'https://mirror.yandex.ru/archlinux/iso/2021.05.01/archlinux-2021.05.01-x86_64.iso',
    'x86_64',
    792014848,
    '2021.05.01'
  ),
  (
    'https://mirror.yandex.ru/archlinux/iso/2021.06.01/archlinux-2021.06.01-x86_64.iso',
    'x86_64',
    811937792,
    '2021.06.01'
  ),
  (
    'https://mirror.yandex.ru/archlinux/iso/2021.07.01/archlinux-2021.07.01-x86_64.iso',
    'x86_64',
    817180672,
    '2021.07.01'
  ),
  (
    'https://mirror.yandex.ru/archlinux/iso/archboot/2020.07/archlinux-2020.07-1-archboot-network.iso',
    'x86_64',
    516947968,
    '2020.07'
  ),
  (
    'https://mirror.yandex.ru/archlinux/iso/archboot/2020.07/archlinux-2020.07-1-archboot.iso',
    'x86_64',
    1280491520,
    '2020.07'
  )
]
```

## 📦  Miscellaneous

### **No hosting devices** error

If your device doesn't support image hosting, try [this Magisk module](https://github.com/overzero-git/DriveDroid-fix-Magisk-module)

### nginx rewrite for okhttp

Use this snippet if you decided to self-host a repository with a website and you wanna access repo.json only by hostname via DriveDroid app since it uses okhttp. Place the next lines in server section of your config.

If you self-host a repository with a website and want the repo.json file accessible only by hostname, place the following snippet inside the `server` section of your **nginx** configuration:

```nginx
location = / {
  if ($http_user_agent ~* 'okhttp') {
    rewrite ^/(.*)$ /repo.json break;
  }
}
```
