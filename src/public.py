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


__all__ = ["bs", "json", "re", "requests",
           "get_iso_arch", "get_iso_size", "logger"]
