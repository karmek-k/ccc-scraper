from bs4 import BeautifulSoup

from scraper.constants import get_toc_url
from scraper.resources import get_page


toc_page = get_page(get_toc_url())
