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

    return response

if __name__ == "__main__":
    song_title = "Afreen"
    song_title = song_title.split()
    
    print(Lyrics(song_title))