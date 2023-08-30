from sys import stderr
import os
import re

import requests

import downloader.constants as constants
from downloader.utils import die
from downloader.errors import RequestError


ROOT_DIR = constants.RESOURCE_ROOT_DIR


def _none_to_empty(string=None):
    """Returns an empty string if `string is None`, else returns the string unchanged"""

    return '' if string is None else string

def make_path(name=None, subdirectory=None):
    """Builds the path to a resource or a subdirectory"""

    # make sure it ends with a slash
    root = ROOT_DIR if ROOT_DIR[-1] == '/' else f'{ROOT_DIR}/'

    # `None` to empty string
    name = _none_to_empty(name)
    subdirectory = _none_to_empty(subdirectory)

    return os.path.join(ROOT_DIR, subdirectory, name)


def get_resource_path(name, subdirectory=None):
    """Returns the path of a resource, or `None` if there is no such resource"""

    maybe_path = make_path(name, subdirectory)    

    if os.path.isfile(maybe_path):
        return maybe_path
    
    return None


def write_resource(name, content, subdirectory=None):
    """Adds a new resource file. Creates the resource directory if it does not exist"""

    path = make_path(name, subdirectory)
    directory, _ = os.path.split(path)

    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(path, 'w') as fp:
        fp.write(content)


def get_page(url, subdirectory=None):
    """Loads the page resource content. Downloads the page if it is required"""

    resource_regex = r'^http://[\w.]+/(.*)$'
    resource = re.findall(resource_regex, url)[0]

    resource_path = get_resource_path(resource, subdirectory)

    if resource_path is not None:
        with open(resource_path) as fp:
            return fp.read()

    response = requests.get(url)

    if not response.ok:
        raise RequestError(response)
    
    response.encoding = constants.SITE_ENCODING
    write_resource(resource, response.text, subdirectory)

    return response.text
    

def open_resource(name, subdirectory=None, mode='r'):
    """
    Opens a resource file using the `open()` function.
    Raises a `FileNotFoundError` if the resource could not be found
    """

    path = get_resource_path(name, subdirectory)
    if path is None:
        raise FileNotFoundError(f'Did not find file: {make_path(name, subdirectory)}')
    
    return open(path, mode)


def list_resources(subdirectory=None):
    """
    Returns an iterable object of resources in the root directory.
    If `subdirectory` is given, then lists resources only in that subdirectory.
    """

    def is_resource_callback(name):
        return os.path.isfile(make_path(name, subdirectory))
    

    subdirectory_path = make_path(subdirectory=subdirectory)
    print(subdirectory_path)

    return filter(is_resource_callback, os.listdir(subdirectory_path))
    