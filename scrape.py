import re

from downloader.resources import list_resources, open_resource
from downloader.constants import RESOURCE_FOOTNOTES


def scrape_footnotes(html):
    """Scrape footnotes from a HTML file into a list of pairs"""

    regex = r"""<a name=\"(\d+)\"><\/a>
<font color=red><b>\d+<\/b></font>  &nbsp;&nbsp;(.+)<br><br>"""

    return re.findall(regex, html, re.I)


# parse footnotes
# print(list(list_resources(RESOURCE_FOOTNOTES)))

with open_resource('przypisy-1-1.htm', 'footnotes') as fp:
    html = fp.read()
    scrape_footnotes(html)
