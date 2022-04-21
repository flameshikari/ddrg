import json
import os
import re
from time import sleep, strftime


try:
    import toml
    import requests
    # from bs4 import BeautifulSoup as bs
    from markdown2 import markdown
    from fake_useragent import UserAgent as user_agent
    from packaging.version import Version as check_version
    from termcolor import colored


except ImportError as error:
    print(f"{error}. Did you install packages from requirements.txt?")
    exit(1)

# https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
DEFAULT_TIMEOUT = 10 # seconds
retries = requests.packages.urllib3.util.retry.Retry(total=3, status_forcelist=[429, 500, 502, 503, 504])
rq = requests.Session()
rq.mount("http://",  requests.adapters.HTTPAdapter(max_retries=retries))
rq.mount("https://", requests.adapters.HTTPAdapter(max_retries=retries))


def logger(message, level=1):
    """Simple logger with log levels and current time."""
    levels = {0: colored('done', 'green'),
              1: colored('info', 'blue'),
              2: colored('fail', 'red')}
    current_time = strftime("%H:%M:%S")
    template = "[{time}] [{level}] {message}"
    print(template.format(time=current_time,
                          level=levels[level],
                          message=message))

from parsers import get
from main import test

__all__ = ["json", "re", "rq", "requests", "check_version", "get", "user_agent", "test"]
