#https://www.youtube.com/results?search_query=tree
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from messages import n # New Line or \n, in a whatsapp friendly format
from sender import sendMessage


def video(search=''):
    if isinstance(search, list):
        search_item = '+'.join(search)
        search = " ".join(search)
    elif search == '':
        search_item = "India"
        search = "India"
    else:
        search_item = search

    # search = search.replace(" ", "+")

    base_url = "https://www.youtube.com"
    query = f"/results?search_query={search_item}"

    soup = BeautifulSoup(
        requests.get(base_url + query).content,    # Web Page to Open
        'html.parser'           # Parser to use
    )
    results = soup.find_all('a',{'class':'yt-uix-sessionlink'}) # Get all contents from the Session Links

    resp = []
    vid_counter = 0
    sub = {
        1:'st',
        2:'nd',
        3:'rd'
    }

    for link in results:
        vid_link = link.get("href")
        if "watch" in vid_link:
            vid_counter+=1
            resp.append(f"The {vid_counter}{sub[vid_counter]} most relevent Video reguarding --> {search} : "+ n + base_url + vid_link)
        
        if len(resp) == 3:
            break
    
    if len(resp) == 0:
        resp = "No Response From the Server, please Try Again.... "

    return resp

def download_video(search=""):
    pass

    
if __name__ == '__main__':
    search = input("Enter what to Search : ")
    search = search.split(' ')

    response = video(search=search)

    if isinstance(response,list):
        sendMessage(msg="\n\n".join(response[:2]))

        if len(response)>4:
            for video in response[2:-2]:
                sendMessage(msg=video)

        sendMessage(msg="\n\n".join(response[-2:]))
    else:
        sendMessage(msg=response)
    print(response)