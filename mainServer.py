from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello():
    resp = MessagingResponse()
    resp.message("Hello World")
    return str(resp)

@app.route("/sms", methods=['POST'])
def main():
    msg = request.form.get('Body')

    msg = msg.lower()

    # print(msg)

    resp = MessagingResponse()
    resp.message(msg[)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
