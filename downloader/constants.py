BASE_URL = 'http://www.katechizm.opoka.org.pl'
PART_NUMBERS_ROMAN = ['I', 'II', 'III', 'IV']

# subdirectories
RESOURCE_CATECHISM = 'catechism'
RESOURCE_FOOTNOTES = 'footnotes'


def get_url(resource):
    return f'{BASE_URL}/{resource}'


def get_toc_url():
    return get_url('spistr.htm')
