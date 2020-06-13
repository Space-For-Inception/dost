from bs4 import BeautifulSoup
import requests

def news():
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

    res = requests.get(url)

    soup = BeautifulSoup(res.content , 'html.parser')
    data = soup.find_all('article' , {'jslog':'85008'})
    for ele in data[0:10]:
        return ele+'\n\n'


if __name__ == '__main__':
    news()    
    