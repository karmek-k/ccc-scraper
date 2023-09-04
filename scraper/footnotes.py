import json
import re

from downloader.resources import Resource
from scraper.constants import RESOURCE_FILE_FOOTNOTES, RESOURCE_SCRAPED


def scrape_footnotes(html):
    """Scrape footnotes from a HTML file into a list of pairs"""

    regex = r"""<a name=\"(\d+)\"><\/a>
.+&nbsp;&nbsp;(.+)<br><br>"""

    return re.findall(regex, html, re.I)


def add_footnotes(html, footnote_dict):
    """Adds footnote keys to a dictionary"""

    for k, v in scrape_footnotes(html):
        footnote_dict[k] = v


def scrape_all_footnotes(footnote_subdirectory):
    footnotes = {}
    for resource in Resource.list_resources(footnote_subdirectory):
        add_footnotes(resource.read(), footnotes)
    
    return footnotes
        

def save_footnotes(footnotes, resource):
    footnotes_json = json.dumps(footnotes, ensure_ascii=False)
    
    resource.content = footnotes_json
    resource.save()


def has_footnotes_saved():
    return Resource.get_path(RESOURCE_FILE_FOOTNOTES, RESOURCE_SCRAPED) is not None
