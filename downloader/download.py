import re

import requests

from downloader.errors import RequestError
from downloader.constants import SITE_ENCODING
from downloader.resources import Resource


def get_page(url, subdirectory=None):
    """Loads the page resource content. Downloads the page if it is required"""

    resource_regex = r'^http://[\w.]+/(.*)$'
    resource_name = re.findall(resource_regex, url)[0]

    resource = Resource(resource_name, subdirectory)

    if Resource.is_saved(resource.name, resource.subdirectory):
        return resource.read()
    
    page_content = download_content(url, SITE_ENCODING)

    resource.content = page_content
    resource.save()
    
    return page_content


def download_content(url, encoding='UTF-8'):
    """Downloads a webpage"""

    resp = requests.get(url)

    if not resp.ok:
        raise RequestError(resp)
    
    resp.encoding = SITE_ENCODING

    return resp.text
