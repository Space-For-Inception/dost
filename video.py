#https://www.youtube.com/results?search_query=tree
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def video(search="#"):
    search =search.split(' ')
    
    if isinstance(search, list):
        search = '+'.join(search)

    base_url = "https://www.youtube.com"

    print(f"got to : {base_url}")

    query = f"/results?search_query={search}"
    
    print(f"Query Created : {base_url+query}")

    soup = BeautifulSoup(
        urlopen(base_url + query).read(),    # Web Page to Open
        'html.parser'           # Parser to use
    )
    
    results = soup.find_all('a',{'class':'yt-uix-sessionlink'}) # Get all contents from the Session Links
    
    resLen = len(results)

    print(f"Found {resLen} Result{'' if resLen == 1 else 's'}")

    for link in results:
        vid_link = link.get("href")
        if "watch" in vid_link:
            return base_url + vid_link
    
if __name__ == '__main__':
    print(video(search="How to make Aloo ki sabji"))