from downloader.constants import get_toc_url, get_url, RESOURCE_CATECHISM, RESOURCE_FOOTNOTES
from downloader.download import get_page
from downloader.resources import Resource
from downloader.errors import RequestError
from downloader.content import make_soup, anchors_to_resource_names, find_footnote_resource_names


def download(name, subdirectory=None):
    """Downloads and saves a page. Returns its contents in plain text"""

    resource = Resource(name, subdirectory)

    print(f'Downloading {resource.name}')

    try:
        return get_page(get_url(resource), subdirectory)
    except RequestError as e:
        print(f'Failed to download {resource.name} - status {e.response.status_code}')


print('Downloading table of contents...')

toc_page = get_page(get_toc_url())
toc_soup = make_soup(toc_page)

anchors = toc_soup.find_all('a')

# download all chapters in the table of contents
for resource_name in anchors_to_resource_names(anchors):
    html = download(resource_name, RESOURCE_CATECHISM)

    # find all footnote indexes in the chapter and download them
    footnotes = find_footnote_resource_names(html)
    for footnote in footnotes:
        download(footnote, RESOURCE_FOOTNOTES)

print('Done')
