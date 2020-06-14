import requests
from bs4 import BeautifulSoup


def covid(search = ''):
    
    if isinstance(search, list):
        search_item = '-'.join(search)
        search = " ".join(search)
    elif search == '':
        search_item = "India"
        search = "India"
    else:
        search_item = search

    url = "https://www.worldometers.info/coronavirus/country/"+search_item
    res = requests.get(url)
    soup = BeautifulSoup(res.content , 'html.parser')

    getting = ""
    final = []

    for data in soup.find_all('div' , id="maincounter-wrap"):
        result = data.text.strip().split('\n\n')
        result = '\t'.join(result)

        final.append(result)

    final = '\n\n'.join(final)+f"\n\n\n\nFor more information on {search}, visit : " + url
    
    return final


if __name__ == '__main__':
    # search = "india"
    print(covid())