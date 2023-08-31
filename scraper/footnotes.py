import json
import re

from downloader.resources import list_resources, write_resource, get_resource_path, get_resource
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
    for res in list_resources(footnote_subdirectory):
        html = get_resource(res, footnote_subdirectory)
        
        add_footnotes(html, footnotes)
    
    return footnotes
        

def save_footnotes(footnotes, resource, subdirectory=None):
    footnotes_json = json.dumps(footnotes, ensure_ascii=False)
    write_resource(resource, footnotes_json, subdirectory=subdirectory)


def has_footnotes_saved():
    return get_resource_path(RESOURCE_FILE_FOOTNOTES, RESOURCE_SCRAPED) is None
