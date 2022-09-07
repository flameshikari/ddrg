from main import *  # noqa


def init():

    values = []
    url_version = 'https://distrowatch.com/table.php?distribution=popos'
    url_base = 'https://api.pop-os.org/builds/{}/{}'
    regexp_version = re.compile(r'<td class="TablesInvert">(\d+\.\d+)</td>')
    response = str(rq.get(url_version).text)
    iso_versions = sorted(set(re.findall(regexp_version, response)), reverse=True)

    for iso_version in iso_versions:
        for driver in ['intel', 'nvidia']:
            try:

                url = url_base.format(iso_version, driver)
                response = json.loads(rq.get(url).text)

                iso_url = response['url']
                iso_arch = get.arch(iso_url)
                iso_size = response['size']
                iso_version = response['version']

                values.append((iso_url, iso_arch, iso_size, iso_version))

            except: continue
    
    return values