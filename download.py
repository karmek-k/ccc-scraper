from downloader.constants import get_toc_url, get_url, RESOURCE_CATECHISM, RESOURCE_FOOTNOTES
from downloader.resources import get_page, make_path
from downloader.errors import RequestError
from downloader.content import make_soup, anchors_to_resources, find_footnote_resources


def download(resource, subdirectory=None):
    """Downloads and saves a resource. Returns its contents in plain text"""

    print(f'Downloading {make_path(resource, subdirectory)}')

    try:
        return get_page(get_url(resource), subdirectory)
    except RequestError as e:
        print(f'Failed to download {resource} - status {e.response.status_code}')


print('Downloading table of contents...')

toc_page = get_page(get_toc_url())
toc_soup = make_soup(toc_page)

anchors = toc_soup.find_all('a')

# download all chapters in the table of contents
for resource in anchors_to_resources(anchors):
    html = download(resource, RESOURCE_CATECHISM)

    # find all footnote indexes in the chapter and download them
    footnotes = find_footnote_resources(html)
    for footnote in footnotes:
        download(footnote, RESOURCE_FOOTNOTES)

print('Done')
