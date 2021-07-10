<p align="center">
  <a href="https://www.drivedroid.io/">
	  <img src="https://www.drivedroid.io/images/feature.svg" width="400" alt="">
  </a>
</p>
  <h1 align="center">Repository Generator</h1>
  <p align="center">Generate a repository for the app that allow boot a PC using ISO files stored on your Android phone</p>
    <a href="https://play.google.com/store/apps/details?id=com.softwarebakery.drivedroid">
    <p align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" width="150" alt="">
    </p>
  </a>
</p>

<br>

# To-Do

- [ ] Option to generate a webpage
- [ ] Option to select mirrors (currently uses mirrors based in Russia)

# Requirements

Python 3.6+ with packages included in [requirements.txt](./requirements.txt).

I recommend to create a venv then install packages there.

# Usage

```bash
python src/main.py [-o output_directory]
```

# How to add scraper

Create a folder in `src/distros` with next structure:

```
distro_name
├── info.toml
├── logo.png
└── scraper.py
```

Let's take a look for every file.

### `info.toml`

```toml
name = "Distro Name" # name of distro
url  = "https://example.com" # official site
```

### `logo.png`

Should be 128x128px with transparent background.

![](./src/misc/fallback_logo.png)

### `scraper.py`

```python
# example for Arch Linux

# the scraper can be written as you like,
# as long as it returns the desired values.
# we can always improve it


from public import * # should be specified


base_urls = [
    "https://mirror.yandex.ru/archlinux/iso/",
    "https://mirror.yandex.ru/archlinux/iso/archboot/"
]


def init(): # should be named 'init'
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for version in html.find_all("a"):
            version = version.get("href")
            if version.startswith("202"):
                html = bs(requests.get(base_url + version)
                                  .text, "html.parser")
                for filename in html.find_all("a"):
                    filename = filename.get("href")
                    if filename.endswith(".iso"):
                        iso_url = base_url + version + filename # string
                        iso_arch = get_iso_arch(iso_url) # string
                        iso_size = get_iso_size(iso_url) # integer
                        iso_version = version[:-1] # string
                        array.append((iso_url, iso_arch,
                                      iso_size, iso_version))


    # always should return tuple of tuples (tuples contains
    # 'iso_url, iso_arch, iso_size, iso_version' in order)

    return array
```
