import re

from bs4 import BeautifulSoup


def make_soup(html):
    """Creates a `BeautifulSoup` object"""

    return BeautifulSoup(html, features='html.parser')


def anchors_to_resource_names(anchors):
    """Transform anchors from `soup.find_all('a') to chapter resource names"""

    anchor_hrefs = map(lambda a: a['href'].replace('rkkk', 'kkk'), anchors)
    return filter(lambda href: href.startswith('kkk'), anchor_hrefs)


def find_footnote_resource_names(html):
    """Finds footnote resources in a HTML document"""

    soup = make_soup(html)
    anchors = soup.find_all('a')

    resources = map(lambda a: a.get('href', ''), anchors)

    footnotes = set()
    regex = r'^([^#]+)(#[0-9]+)?$'
    for footnote in filter(lambda r: r.startswith('przypisy'), resources):
        resource = re.search(regex, footnote).group(1)
        footnotes.add(resource)
    
    return footnotes
