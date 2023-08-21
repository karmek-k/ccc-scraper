from downloader.constants import get_toc_url, BASE_URL
from downloader.resources import get_page
from downloader.errors import RequestError
from downloader.content import make_soup, anchors_to_resources, find_footnote_resources


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