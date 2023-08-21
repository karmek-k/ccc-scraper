from sys import stderr
import os
import re

import requests

from downloader.utils import die
from downloader.errors import RequestError


ROOT_DIR = 'download/'


def get_resource_path(name):
    """Returns the path of a resource, or `None` if there is no such resource"""

    maybe_path = f'{ROOT_DIR}/{name}'
    
    if os.path.isfile(maybe_path):
        return maybe_path
    
    return None


def write_resource(name, content):
    """Adds a new resource file. Creates the resource directory if it does not exist"""

    if not os.path.exists(ROOT_DIR):
        os.mkdir(ROOT_DIR)

    with open(f'{ROOT_DIR}/{name}', 'w') as fp:
        fp.write(content)


def get_page(url):
    """Loads the page resource content. Downloads the page if it is required"""

    resource_regex = r'^http://[\w.]+/(.*)$'
    resource = re.findall(resource_regex, url)[0]

    resource_path = get_resource_path(resource)

    if resource_path is not None:
        with open(resource_path) as fp:
            return fp.read()

    response = requests.get(url)

    if not response.ok:
        raise RequestError(response)
    
    response.encoding = 'iso-8859-2'
    write_resource(resource, response.text)

    return response.text
    
