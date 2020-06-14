from bs4 import BeautifulSoup
import requests

def news():
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

    res = requests.get(url)

    soup = BeautifulSoup(res.content , 'html.parser')
    data = soup.find_all('article' , {'jslog':'85008'})

    final_news_list = ''

    for ele in data[:5]:
        final_news_list+='\n\n'+ele.text
    
    return "The Top 3 News of the Day are :\n\n"+final_news_list


if __name__ == '__main__':
    print(news())
