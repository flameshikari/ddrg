from public import *  # noqa


base_urls = [
  "https://mirror.yandex.ru/debian-cd/current-live/amd64/iso-hybrid/",
  "https://mirror.yandex.ru/debian-cd/current-live/i386/iso-hybrid/",
  "https://mirror.yandex.ru/debian-cd/current/amd64/iso-bd/",
  "https://mirror.yandex.ru/debian-cd/current/amd64/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/amd64/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/arm64/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/arm64/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/armel/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/armel/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/i386/iso-bd/",
  "https://mirror.yandex.ru/debian-cd/current/i386/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/i386/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/mips/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/mips/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/mips64el/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/mips64el/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/mipsel/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/mipsel/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/multi-arch/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/ppc64el/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/ppc64el/iso-dvd/",
  "https://mirror.yandex.ru/debian-cd/current/s390x/iso-cd/",
  "https://mirror.yandex.ru/debian-cd/current/s390x/iso-dvd/"
]


def init():
    array = []
    for base_url in base_urls:
        html = bs(requests.get(base_url).text, "html.parser")
        for filename in html.find_all("a"):
            filename = filename.get("href")
            if filename.endswith(".iso"):
                iso_url = base_url + filename
                iso_arch = get_iso_arch(iso_url)
                iso_size = get_iso_size(iso_url)
                iso_version = re.search(r"-(\d+.\d+.\d+)", iso_url).group(1)
                array.append((iso_url, iso_arch, iso_size, iso_version))
    return array
