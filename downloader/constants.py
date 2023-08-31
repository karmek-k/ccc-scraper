RESOURCE_ROOT_DIR = 'resources/'
BASE_URL = 'http://www.katechizm.opoka.org.pl'
PART_NUMBERS_ROMAN = ['I', 'II', 'III', 'IV']

SITE_ENCODING = 'iso-8859-2'

# subdirectories
RESOURCE_CATECHISM = 'catechism'
RESOURCE_FOOTNOTES = 'footnotes'

# resource names
RESOURCE_NAME_TOC = 'spistr.htm'


def get_url(resource):
    """Provides a remote URL to a resource"""

    return f'{BASE_URL}/{resource}'


def get_toc_url():
    """URL for the `table of contents` resource"""

    return get_url(RESOURCE_NAME_TOC)
