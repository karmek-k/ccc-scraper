import json
import re

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
        'source': get_url(resource),
        'paragraphs': [],
    }

    # TODO: improve the crude implementation
    # FIXME: does not collect paragraphs without numbers
    for paragraph in soup.find_all('p', attrs={'align': 'justify'}):
        # remove anchors
        for anchor in paragraph.find_all('a'):
            try:
                if not anchor['name'].startswith('p'):
                    anchor.decompose()
            except:
                anchor.decompose()
        
        # remove strikelines
        for strike in paragraph.find_all('strike'):
            strike.decompose()
        
        try:
            number_tag = paragraph.b.extract()
            number = number_tag.text.strip()
        except:
            pass

        if number.isdecimal():
            text = paragraph.text.strip().replace('\n', ' ')
            # TODO: do it with one regex
            text = re.sub(r' {2,}', ' ', text)
            text = re.sub(r' +\.', '.', text)
            text = re.sub(r' +\,', ',', text)

            # append if `text` is not empty
            if text.strip():
                result['paragraphs'].append({
                    'number': number,
                    'text': text,
                })

    for p in result['paragraphs']:
        print(p['number'])
        print(p['text'])
        print()
    # print(result)
    break
