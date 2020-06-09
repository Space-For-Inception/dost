import requests
from bs4 import BeautifulSoup

def wiki(search=''):

    if isinstance(search, list):
        search_item = '_'.join(search)
        search = " ".join(search)
    elif search == '':
        search_item = "India"
        search = "India"
    else:
        search_item = search
    
    url = "https://en.wikipedia.org/wiki/"+search_item
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    ele = soup.find('div', id='mw-content-text')                    # find the paragraph with content.
    result = ele.find_all('p')[0:2]

    text_result = "\n".join([r.text for r in result])

    return text_result + f"\n\nFor more information on {search} visit : "+url

if __name__ == '__main__':
    search = "Amul Masti"

    search = search.split(' ')

    print(wiki(search))
