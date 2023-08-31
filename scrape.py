from downloader.resources import get_resource
from downloader.constants import RESOURCE_FOOTNOTES
from scraper.constants import RESOURCE_SCRAPED, RESOURCE_FILE_FOOTNOTES
from scraper.footnotes import scrape_all_footnotes, save_footnotes, has_footnotes_saved


def make_footnotes():
    """Scrapes and saves footnotes, if needed. Returns a footnote dictionary"""

    if has_footnotes_saved():
        footnotes = scrape_all_footnotes(RESOURCE_FOOTNOTES)
        save_footnotes(footnotes, RESOURCE_FILE_FOOTNOTES, RESOURCE_SCRAPED)

        return footnotes

    return get_resource(RESOURCE_FILE_FOOTNOTES, RESOURCE_SCRAPED)


footnotes = make_footnotes()
