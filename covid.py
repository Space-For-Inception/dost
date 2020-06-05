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
        result = data.text 
        listing.append(result)
    
    
    for correcting in listing:
        if(correcting != "\n"):
            getting = getting+correcting
            print(getting)
        getting = ""
        # for ass in correcting:
        #     if(ass!= "\n"):
        #         pass
            
            
        #     final.append(ass)

    # print(final)    
    # for show in final:
    #     print(show + "\n")




if __name__ == '__main__':
    search = "india"
    covid(search)