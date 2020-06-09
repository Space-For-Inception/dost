from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

from messages import Main_Menu, Error_Reply
from wiki import wiki
from covid import covid
from video import video

def menu(nothing:str=''):
    return Main_Menu

def error(nothing:str=''):
    return Error_Reply

validInputs = {
    "help":menu,
    "info":menu,
    "wiki":wiki,
    "video":video,
    "covid":covid,
    "error":error
}




################################################################################
################################################################################

app = Flask(__name__)

@app.route("/")
def hello():
    resp = MessagingResponse()
    resp.message("Hello World")
    return str(resp)

@app.route("/sms", methods=['POST'])
def main():
    print(request.form)
    msg = request.form.get('Body').lower().split()

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

    resp = MessagingResponse()
    resp.message(msg)

    return str(resp)

################################################################################
################################################################################








if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
