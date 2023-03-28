from main import *  # noqa

from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from os import devnull


Options = Options()
Options.headless = True

def init():

    values = []
    regexp_version = re.compile(r'-(\d+T\d+Z)\.iso')
    url_base = 'https://us-central.manta.mnx.io'
    url_version = 'https://us-central.manta.mnx.io/Joyent_Dev/public/SmartOS/smartos.html'

    try:
        driver = webdriver.Firefox(service_log_path=devnull, options=Options, executable_path='geckodriver.exe')
        driver.get(url_version)
        driver_wait(driver, 3).until(ec.presence_of_element_located((by.CLASS_NAME, 'links')))
        source = driver.page_source
    finally:
        driver.quit()

    pattern = re.compile(r'href=\"(.*?)\"', re.S)
    iso_urls = [url for url in re.findall(pattern, str(source)) if url.endswith('.iso')]

    for iso_url in iso_urls:

        iso_url = url_base + iso_url
        iso_arch = get.arch(iso_url)
        iso_size = get.size(iso_url)
        iso_version = re.search(regexp_version, iso_url).group(1)
        values.append((iso_url, iso_arch, iso_size, iso_version))

    return values
