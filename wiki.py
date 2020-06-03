import requests
from bs4 import BeautifulSoup
def wiki():
    res = requests.get("http://www.wikipedia.com")
    soup = BeautifulSoup(res.text, 'lxml')
    titl= soup.select('title')
    print(titl[0].text)




if __name__ == '__main__':
    wiki()