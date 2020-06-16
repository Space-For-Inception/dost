from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

from messages import shortMenu, MainMenu, ErrorReply, introPage, n
from wiki import wiki
from covid import covid
from video import video, download_video
from sender import sendMessage
from lyrics import getLyrics
from news import news

from time import sleep

def menu(nothing:str=''):
    return shortMenu

def longMenu(nothing:str=''):
    return MainMenu

def error(nothing:str=''):
    return ErrorReply



validInputs = {
    "help":menu,
    "info":menu,
    "help-all":longMenu,
    "wiki":wiki,
    "video":video,
    "covid":covid,
    "news":news,
    "youtube":video,
    "dvideo":download_video,
    "lyrics":getLyrics,
    "error":error
}




################################################################################
################################################################################

app = Flask(__name__)

@app.route("/")
def hello():
    return introPage

@app.route("/sms", methods=['POST'])
def main():
    From    = request.form.get('From')
    msg     = request.form.get('Body').lower().split()

    if len(msg) == 1:
        arg = ''
    elif len(msg) == 2:
        arg = msg[1]
    else:
        arg = msg[1:]

    msg = msg[0]

    if msg in validInputs:
        msg = validInputs[msg](arg)
    else:
        msg = validInputs["error"]()

    if isinstance(msg, list):

        for resp in msg:
            sendMessage(clientPhoneNo=From,msg=resp)
            sleep(0.5)
        
        resp_message = "Type help for more options."
    else:
        resp_message = msg + "\n\nType help for more options."

    sendMessage(clientPhoneNo=From, msg=resp_message)
    
    return str(resp_message)

################################################################################
################################################################################








if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
