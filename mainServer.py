from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

from messages import Main_Menu, Error_Reply
from wiki import wiki
from covid import covid

def menu(str:nothing):
    return Main_Menu

def error(str:nothing):
    return Error_Reply

validInputs = {
    "help":menu,
    "info":menu,
    "wiki":wiki,
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

    if msg[0] in validInputs:
        msg = validInputs[msg[0](' '.join(msg[1:]))]
    else:
        msg = validInputs[msg["error"](' '.join(msg[1:]))]

    resp = MessagingResponse()
    resp.message(msg)

    return str(resp)

################################################################################
################################################################################








if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
