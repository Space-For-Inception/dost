import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen


def wiki(search):
    count=0
    url = "https://en.wikipedia.org/wiki/"+search
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    



    ele = soup.find('div', id='mw-content-text')
    for para in ele:
        count = count+1
        para = ele.find_all('p')[count]
        result = para
        getit = para.text
        getit = getit.split(" ")
        len_of_string= len(getit)
        for getit in range(0,len_of_string):
            if(getit == search):
                break
    print(result.text)



if __name__ == '__main__':
    search = "bird"
    wiki(search)