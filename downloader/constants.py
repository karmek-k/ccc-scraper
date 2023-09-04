import os


RESOURCE_ROOT_DIR = 'resources/'
BASE_URL = 'http://www.katechizm.opoka.org.pl'
PART_NUMBERS_ROMAN = ['I', 'II', 'III', 'IV']

SITE_ENCODING = 'iso-8859-2'

# subdirectories
DIR_CATECHISM = 'catechism'
DIR_FOOTNOTES = 'footnotes'

# resource names
RESOURCE_NAME_TOC = 'spistr.htm'


def get_url(resource):
    """Provides a remote URL to a resource"""

    return os.path.join(BASE_URL, resource.name)


def get_toc_url():
    """URL for the `table of contents` resource"""

    return os.path.join(BASE_URL, RESOURCE_NAME_TOC)
