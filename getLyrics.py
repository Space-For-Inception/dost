from lyrics_extractor import Song_Lyrics


GCS_API_KEY = "AIzaSyCOqTGehUFkYiZKFAQ_K1hiEgF_ZoYVmsk"
GCS_ENGINE_ID = "016631629619703458515:cnu29awb2ub"


def Lyrics(song_title=""):
    if isinstance(song_title, list):
        song_title = "%20".join(song_title)
    elif song_title == '':
        song_title = "India"
    
    extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    song_title, song_lyrics = extract_lyrics.get_lyrics(song_title)

    response = ''

    if song_lyrics != '':
        response = f"Lyrics for {song_title} is as follows : \n\n{song_lyrics}"
    else:
        response = f"No lyrics found for {song_title}"

    respList = []

    if len(response)>1000:
       response = response.split("\n")
       #for seg in range(1, len(response)-100):
           

    return response

if __name__ == "__main__":
    from sender import sendMessage

    song_title = "Vande Mataram"
    song_title = song_title.split()

    response = Lyrics(song_title)

    if isinstance(response,list):
        sendMessage(msg="\n\n".join(response[:2]))

        for stanza in response[2:-2]:
            sendMessage(msg=stanza)

        sendMessage(msg="\n\n".join(response[-2:]))
    else:
        sendMessage(msg=response)

    
    print(response)
