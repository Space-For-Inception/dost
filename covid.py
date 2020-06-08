import requests
from bs4 import BeautifulSoup


def covid(search):
    url = "https://www.worldometers.info/coronavirus/country/"+search
    res = requests.get(url)
    COUNT = 0 
    soup = BeautifulSoup(res.content , 'html.parser')
    # cases = soup.find('div', id= 'content-inner')
    listing = []

    getting = ""
    final = []

    for data in soup.find_all('div' , id="maincounter-wrap"):
        result = data.text.strip().split('\n\n')
        result = '\t'.join(result)
        listing.append(result)
    
    for correcting in listing:
        if(correcting != "\n"):
            getting = getting+correcting

        final.append(getting)
        getting = ""

    final = ['\n\n'.join(final), "\n\nFor more information, visit : " + url]
    
    return '\n\n'.join(final)




if __name__ == '__main__':
    search = "india"
    print(covid(search))