import requests
from bs4 import BeautifulSoup

def wiki(search="India"):
    search = search.split(' ')

    if isinstance(search, list):
        search = '_'.join(search)
    
    url = "https://en.wikipedia.org/wiki/"+search
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    ele = soup.find('div', id='mw-content-text')                    # find the paragraph with content.
    result = ele.find_all('p')[0:2]

    text_result = "\n".join([r.text for r in result])

    return text_result + f"\n\nFor more information visit : "+url

if __name__ == '__main__':
    search = "Amul Masti"
    print(wiki(search))
