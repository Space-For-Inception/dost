from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

from messages import Main_Menu, Error_Reply, intro_page, n
from wiki import wiki
from covid import covid
from video import video
from sender import sendMessage

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
    "youtube":video,
    "error":error
}




################################################################################
################################################################################

app = Flask(__name__)

@app.route("/")
def hello():
    return intro_page

@app.route("/sms", methods=['POST'])
def main():
    To      = request.form.get('To')[8:]
    From    = request.form.get('From')[8:]

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

    if isinstance(msg, list):
        resp_message = ['']

        for msg_part in msg[:-1]:
            if len(msg_part)+len(resp_message[-1]) < 1299:
                resp_message[-1]+="\n"+msg_part
            else:
                resp_message.append(msg_part)

        for resp in resp_message:
            sendMessage(clientPhoneNo=To,msg=resp_message)

        resp_message = msg[-1]

    else:
        resp_message = msg

    resp = MessagingResponse()
    resp.message(msg)

    return str(resp)

################################################################################
################################################################################








if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
