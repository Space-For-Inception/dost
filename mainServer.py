'''import sender
from time import sleep
from sender import sendMessage

for i in range(5):
    sendMessage(msg=f'This is cool times {i}')
    sleep(1)

'''

from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello():
    resp = MessagingResponse()
    resp.message("Hello World")
    return str(resp)

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    msg = msg.lower().split()

    print(msg)

    resp = MessagingResponse()
    resp.message(msg)

    return str(resp)

def MusicService(song_name):
    return "\n\n".join(Lyrics(song_name))

def SongVideoService(song_name):
    pass

if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
