from bs4 import BeautifulSoup

from downloader.constants import get_toc_url, BASE_URL
from downloader.resources import get_page


print('Downloading table of contents...')

toc_page = get_page(get_toc_url())
toc_soup = BeautifulSoup(toc_page, features='html.parser')

anchors = toc_soup.find_all('a')
anchor_hrefs = map(lambda a: a['href'].replace('rkkk', 'kkk'), anchors)
chapter_resources = filter(lambda href: href.startswith('kkk'), anchor_hrefs)

for resource in chapter_resources:
    print(f'Downloading {resource}')
    get_page(f'{BASE_URL}/{resource}')

print('Done')