from lyrics_extractor import Song_Lyrics


GCS_API_KEY = "AIzaSyCOqTGehUFkYiZKFAQ_K1hiEgF_ZoYVmsk"
GCS_ENGINE_ID = "016631629619703458515:cnu29awb2ub"


def getLyrics(song_title=""):
    if isinstance(song_title, list):            # Check if input is a list of Words
        song_title = " ".join(song_title)       
    elif song_title == '':                      # Check of input is blank
        song_title = "Vande Mataram"
    
    extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    song_head, song_lyrics = extract_lyrics.get_lyrics(song_title)

    if song_lyrics == '':
        song_head, song_lyrics = extract_lyrics.get_lyrics(song_title)
        
    if song_lyrics == '':
        song_head, song_lyrics = extract_lyrics.get_lyrics(song_title)
    
    if song_lyrics == '':
        song_head, song_lyrics = extract_lyrics.get_lyrics(song_title)

    if song_lyrics == '':
        song_head, song_lyrics = extract_lyrics.get_lyrics(song_title)

    if song_lyrics != '':
        response = f"Lyrics for {song_head} is as follows : \n\n{song_lyrics}"
        response = response.split('\n\n')

    else:
        response ="Err: No lyrics found for " + song_title
    
    return response

if __name__ == "__main__":
    from sender import sendMessage

    song_title = "In the edn"
    song_title = song_title.split()

    msg = getLyrics(song_title)

    # print("/\\"*25,"Starting to Send Messages","/\\"*25)

    if isinstance(msg, list):
        
        # for msg_no, msg_part in enumerate(msg):
        #     print(f"SMS-{msg_no+1}")
        #     # print(f"Sending from inside for : {msg_part}")
        #     sendMessage(msg=msg_part)
        #     print("-"*40)

        msg = "\n\n".join(msg)        
        sendMessage(msg)
        
        msg = "Type help for more options."
    else:
        msg = msg + "\n\nType help for more options."
    
    # print(f"SMS-{msg_no+1}")
    sendMessage(msg=msg)
    # print(f"Response : {msg}")
