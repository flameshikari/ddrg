import json
import os
import re
from time import strftime

try:
    import lxml
    import requests
    import toml
    from bs4 import BeautifulSoup as bs

except ImportError as error:
    print(f"{error}. Did you install packages from requirements.txt?")
    exit(1)


class AndroidFileHost:
    """Based on https://github.com/kade-robertson/afh-dl"""

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def get(url):
        mirror_url = r"https://androidfilehost.com/libs/otf/mirrors.otf.php"
        url_matchers = [re.compile(r"fid=(?P<id>\d+)")]

        for pattern in url_matchers:
            result = pattern.search(url)
            if result is not None:
                file_match = result

        if file_match:
            fid = file_match.group('id')
            init = requests.get("https://androidfilehost.com/?fid={}"
                                .format(fid))

            post_data = {
                "submit": "submit",
                "action": "getdownloadmirrors",
                "fid": fid
            }

            mirror_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/63.0.3239.132 Safari/537.36",

                "Content-Type": "application/x-www-form-urlencoded; "
                                "charset=UTF-8",

                "Referer": "https://androidfilehost.com/?fid={}".format(fid),
                "X-MOD-SBB-CTYPE": "xhr",
                "X-Requested-With": "XMLHttpRequest"
            }

            mirror_data = requests.post(mirror_url,
                                        headers=mirror_headers,
                                        data=post_data,
                                        cookies=init.cookies)
            try:
                mirrors = json.loads(mirror_data.text)
                if not mirrors["STATUS"] == "1" or \
                   not mirrors["CODE"] == "200":
                    return None
                else:
                    mirror_opts = []
                    for mirror in mirrors["MIRRORS"]:
                        mirror_opts.append(AndroidFileHost(**mirror))
            except Exception as e:
                return None

            servers = mirror_opts
            if servers is None:
                return
            return servers[0].url


def logger(message, level=1):
    """Simple logger with log levels and current time."""
    levels = {0: "done",
              1: "info",
              2: "fail"}
    current_time = strftime("%H:%M:%S")
    template = "[{time}] [{level}] {message}"
    print(template.format(time=current_time,
                          level=levels[level],
                          message=message))


def get_iso_size(target):
    """Returns the file size of the target URL in bytes."""
    if target.startswith("http"):
        return int(requests.get(target, stream=True)
                           .headers["Content-Length"])
    else:
        return 0


def get_iso_arch(target):
    """Returns the used processor architecture of the target URL."""

    archs_all = [
        "i386", "amd64",
        "arm64", "arm32", "armhfp", "armhf", "armel", "aarch64",
        "i586", "i686-pae", "i686", "ia64",
        "ppc64le", "ppc64el", "ppc64", "ppcspe", "ppc",
        "mips64el", "mipsel", "mips",
        "s390x", "hppa", "macppc", "alpha", "sparc64",
        "bios", "efi"
    ]

    archs_86_64 = [
        "86_64",
        "86-64",
        "96",
        "archboot"
    ]

    archs_64 = [
        "x64",
        "64bit",
        "dual",
        "64"
    ]

    archs_86 = [
        "x86",
        "x32",
        "32bit",
        "386",
        "32"
    ]

    for arch in archs_all:
        if arch in target:
            return arch

    if any(arch in target for arch in archs_86_64):
        return "x86_64"

    elif any(arch in target for arch in archs_64):
        return "amd64"

    elif any(arch in target for arch in archs_86):
        return "i386"

    elif "powerpc" in target:
        return target.replace("powerpc", "ppc")

    elif "legacy" in target:
        return "bios"

    else:
        return "unk"


get_afh_url = AndroidFileHost.get

__all__ = ["bs", "json", "re", "requests",
           "get_afh_url", "get_iso_arch", "get_iso_size", "logger"]
