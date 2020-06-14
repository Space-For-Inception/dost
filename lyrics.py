from lyrics_extractor import Song_Lyrics


GCS_API_KEY = "AIzaSyCOqTGehUFkYiZKFAQ_K1hiEgF_ZoYVmsk"
GCS_ENGINE_ID = "016631629619703458515:cnu29awb2ub"


def getLyrics(song_title=""):
    if isinstance(song_title, list):
        song_title = " ".join(song_title)
    elif song_title == '':
        song_title = "Vande Mataram"
    
    extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    song_head, song_lyrics = extract_lyrics.get_lyrics(song_title.replace(" ",' '))

    response = ''

    if song_lyrics != '':
        response = f"Lyrics for {song_title} is as follows : \n\n{song_lyrics}"
        response = response.split('\n\n')
        #print(f"Split response : {response}")
    else:
        response = song_head

    if isinstance(response, list):
        resp_message = ['']

        #print(f"response has : {len(response)} elements.")

        for msg_part in response:
            if len(msg_part)+len(resp_message[-1]) < 1299:
                resp_message[-1]+="\n\n"+msg_part
                #print("joining...")
            else:
                resp_message.append(msg_part)
                #print("creating...")
    
    else:
        resp_message = response
    
    #print("Returning : ",resp_message)
    return resp_message

if __name__ == "__main__":
    from sender import sendMessage

    song_title = "Powerless"
    song_title = song_title.split()

    msg = getLyrics()

    if isinstance(msg, list):
        resp_message = msg[:-1]
        
        for resp in resp_message:
            #print(f"Sending from inside for : {resp_message}")
            sendMessage(msg=resp_message)

        resp_message = msg[-1]
    else:
        resp_message = msg
    
    print(f"last response : {resp_message}")
