<br>
<p align="center">
  <img src="../src/website/root/assets/logo.svg" width="250" alt="">
</p>
  <h1 align="center">
    <a target="_blank" href="https://softwarebakery.com/projects/drivedroid">DriveDroid</a> Repository Generator <img src="https://github.com/flameshikari/ddrg/actions/workflows/builder.yml/badge.svg">
  </h1>
</p>

## 🚧 Disclaimer

This tool in under continuous development, but it kinda works. Beware a lot of weird code!

## 💿 Try It Now

Just add the following link to the image repositories in DriveDroid:
```
https://dd.hexed.pw/repo.json
```

## 📝 Writing Scrapers

Create a folder in **[distros](../src/distros)** with the next structure:

```
distro_name
├── logo.png
└── scraper.py
```

If `distro_name` starts with the underscore (e.g. **_disabled**), it will be excluded from scraping.

### `logo.png`

Should be 128x128px with transparent background. Arch Linux **[logo.png](../src/distros/arch/logo.png)** example:

<br><p align="center">
  <img src="../src/distros/arch/logo.png" alt="Arch Linux"/>
</p><br>

### `scraper.py`

A scraper can be written as you like, as long as it returns the desired values: the array of namespaces (namespaces should contain **arch**, **size**, **url**, **version**) and contains `info` variable (a namespace too) with the name and the homepage url of the distro (see the example below).

`from shared import *` at the top of the scraper includes helpful functions and classes from `helpers.py`.

For example, **[Arch Linux](../src/distros/arch/scraper.py)** scraper looks like this:


```python
from shared import *

info = ns(
    name='Arch Linux',
    url='https://archlinux.org',
)

@scraper
def init():
    values = []

    regexp = r'-(\d+.\d+(.\d+)?)'

    target = 'https://mirror.yandex.ru/archlinux/iso/'
    
    exclude = ['archlinux-x86_64', 'arch/', 'latest/']

    for url, size in get.urls(target, exclude=exclude, recursive=True):

        arch = get.arch(url)
        version = get.version(url, regexp)

        values.append(ns(
            arch=arch,
            size=size,
            url=url,
            version=version
        ))

    return values

```

This scraper returns values similar to the following:

```python
[
    namespace(
        arch='x86_64', 
        size=1357545472,
        url='https://mirror.yandex.ru/archlinux/iso/2025.07.01/archlinux-2025.07.01-x86_64.iso',
        version='2025.07.01'
    ),
    namespace(
        arch='x86_64',
        size=1378795520,
        url='https://mirror.yandex.ru/archlinux/iso/2025.08.01/archlinux-2025.08.01-x86_64.iso',
        version='2025.08.01'
    ),
    namespace(
        arch='x86_64',
        size=1506082816,
        url='https://mirror.yandex.ru/archlinux/iso/2025.09.01/archlinux-2025.09.01-x86_64.iso',
        version='2025.09.01'
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
