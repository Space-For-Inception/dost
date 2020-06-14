from twilio.rest import Client
import QBTTXPSE

def getIt(what:str = None):
    QXE = ''
    if what == 'AC':
        key = QBTTXPSE.AC
        QXE += 'AC'
    else:
        key = QBTTXPSE.extra
    for Q in key:
        if len(Q) == 1:
            QXE+= Q
        else:
            QXE+= hex(int(Q)).lstrip('0x')
    return QXE

account_sid = getIt('AC')
auth_token = getIt()

client = Client(account_sid, auth_token) 

def sendMessage(clientPhoneNo:str = '+917798044008', msg:str = 'Hello World'):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body =msg,      
                                to   =f'whatsapp:{clientPhoneNo}'
            )           

if __name__ == "__main__":
    cool = "C"+"O"*2+"L"
    for ch in cool:
        sendMessage(msg=f"*{ch}*")
