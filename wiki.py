import requests
from bs4 import BeautifulSoup


def wiki(search):
    count=0
    url = "https://en.wikipedia.org/wiki/"+search               
    res = requests.get(url)                                         # get the html source code.
    soup = BeautifulSoup(res.content, 'html.parser')

    ele = soup.find('div', id='mw-content-text')                    # find the paragraph with content.

    for para in ele:                                                # it is used to go throught all paragraph.
       
        para = ele.find_all('p')[count]                     
        count = count+1
        result = para
        getit = para.text
        getit = getit.split(" ")
        len_of_string= len(getit)

        for getit in range(0,len_of_string):                        # it will check wheather the paragraph contian data.
            if(getit == search):
                break

    return result.text + f"\n\nFor more information visit : "+url



if __name__ == '__main__':
    search = "tree"
    print(wiki(search))
