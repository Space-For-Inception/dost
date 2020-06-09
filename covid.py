import requests
from bs4 import BeautifulSoup


def covid(search = "India"):
    url = "https://www.worldometers.info/coronavirus/country/"+search
    res = requests.get(url)
    soup = BeautifulSoup(res.content , 'html.parser')

    getting = ""
    final = []

    for data in soup.find_all('div' , id="maincounter-wrap"):
        result = data.text.strip().split('\n\n')
        result = '\t'.join(result)

        final.append(result)

    final = ['\n\n'.join(final), "\n\nFor more information, visit : " + url]
    
    return '\n\n'.join(final)


if __name__ == '__main__':
    # search = "india"
    print(covid())