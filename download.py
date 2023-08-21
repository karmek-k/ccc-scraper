import re

from bs4 import BeautifulSoup

from downloader.constants import get_toc_url, BASE_URL
from downloader.resources import get_page
from downloader.errors import RequestError


def make_soup(html):
    return BeautifulSoup(html, features='html.parser')


def anchors_to_resources(anchors):
    """Transform anchors from `soup.find_all('a') to chapter resource names"""

    anchor_hrefs = map(lambda a: a['href'].replace('rkkk', 'kkk'), anchors)
    return filter(lambda href: href.startswith('kkk'), anchor_hrefs)


def find_footnote_resources(html):
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


def download(resource):
    """Downloads a resource"""

    print(f'Downloading {resource}')

    try:
        return get_page(f'{BASE_URL}/{resource}')
    except RequestError as e:
        print(f'Failed to download {resource} - status {e.response.status_code}')


print('Downloading table of contents...')

toc_page = get_page(get_toc_url())
toc_soup = make_soup(toc_page)

anchors = toc_soup.find_all('a')

for resource in anchors_to_resources(anchors):
    html = download(resource)

    footnotes = find_footnote_resources(html)
    for footnote in footnotes:
        download(footnote)

print('Done')