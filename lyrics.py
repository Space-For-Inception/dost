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

    if song_lyrics != '':
        response = f"Lyrics for {song_title} is as follows : \n\n{song_lyrics}"
        response = response.split('\n\n')

    else:
        response ="Err: No lyrics found for " + song_title

    if isinstance(response, list):
        resp_message = ['']

        for msg_part in response:
            if len(msg_part)+len(resp_message[-1]) < 1298:
                print("joining msg_part : msg_part:",msg_part)
                resp_message[-1]+="\n\n"+msg_part
            else:
                resp_message.append(msg_part)
    else:
        resp_message = response
    
    return resp_message

if __name__ == "__main__":
    from sender import sendMessage

    song_title = "Jana Gana mana"
    song_title = song_title.split()

    msg = getLyrics(song_title)

    if isinstance(msg, list):
        resp_message = msg
        
        for msg_no, resp in enumerate(resp_message):
            print(f"SMS-{msg_no+1}")
            # print(f"Sending from inside for : {resp}")
            sendMessage(msg=resp_message)
            print("-"*40)
        
        msg_no += 1
        resp_message = "Type help for more options."
    else:
        resp_message = msg + "\n\nType help for more options."
    
    print(f"Response : {resp_message}")
    sendMessage(msg=resp_message)
