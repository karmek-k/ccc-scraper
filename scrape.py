import json
import re

from downloader.resources import list_resources, open_resource, write_resource
from downloader.constants import RESOURCE_FOOTNOTES, RESOURCE_SCRAPED


def scrape_footnotes(html):
    """Scrape footnotes from a HTML file into a list of pairs"""

    regex = r"""<a name=\"(\d+)\"><\/a>
.+&nbsp;&nbsp;(.+)<br><br>"""

    return re.findall(regex, html, re.I)


footnotes = {}
for res in list_resources(RESOURCE_FOOTNOTES):
    with open_resource(res, RESOURCE_FOOTNOTES) as fp:
        html = fp.read()
    
    pairs = scrape_footnotes(html)
    print(f'{len(pairs)} footnotes in {res}')
    
    for k, v in pairs:
        footnotes[int(k)] = v
    
footnotes_json = json.dumps(footnotes, ensure_ascii=False)
write_resource('footnotes.json', footnotes_json, subdirectory=RESOURCE_SCRAPED)
