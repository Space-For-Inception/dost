#https://www.youtube.com/results?search_query=tree
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


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

    for link in results:
        vid_link = link.get("href")
        if "watch" in vid_link:
            return f"Here is your Youtube Video for {search} : " + base_url + vid_link
    
if __name__ == '__main__':
    search = input("Enter what to Search : ")
    search = search.split(' ')
    print(video(search=search))