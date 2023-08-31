import json


from downloader.resources import Resource
from downloader.constants import RESOURCE_FOOTNOTES
from scraper.constants import RESOURCE_SCRAPED, RESOURCE_FILE_FOOTNOTES
from scraper.footnotes import scrape_all_footnotes, save_footnotes, has_footnotes_saved


def footnotes_resource():
    return Resource(RESOURCE_FILE_FOOTNOTES, RESOURCE_SCRAPED)


def make_footnotes():
    """Scrapes and saves footnotes, if needed. Returns a footnote dictionary"""

    resource = footnotes_resource()

    if Resource.is_saved(resource.name, resource.subdirectory):
        with resource.open() as f:
            return json.load(f)

    footnotes = scrape_all_footnotes(RESOURCE_FOOTNOTES)
    save_footnotes(footnotes, resource)

    return footnotes


footnotes = make_footnotes()
