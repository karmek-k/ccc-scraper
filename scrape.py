import json

from downloader.content import make_soup
from downloader.resources import Resource
from downloader.constants import DIR_FOOTNOTES, DIR_CATECHISM, get_url
from scraper.constants import DIR_SCRAPED, RESOURCE_FILE_FOOTNOTES
from scraper.footnotes import scrape_all_footnotes, save_footnotes, has_footnotes_saved


def footnotes_resource():
    return Resource(RESOURCE_FILE_FOOTNOTES, DIR_SCRAPED)


def make_footnotes():
    """Scrapes and saves footnotes, if needed. Returns a footnote dictionary"""

    resource = footnotes_resource()

    if Resource.is_saved(resource.name, resource.subdirectory):
        with resource.open() as f:
            return json.load(f)

    footnotes = scrape_all_footnotes(DIR_FOOTNOTES)
    save_footnotes(footnotes, resource)

    return footnotes


footnotes = make_footnotes()


for resource in Resource.list_resources(DIR_CATECHISM):
    html = resource.read()
    soup = make_soup(html)

    result = {
        'source': get_url(resource)
    }

    print(result)
