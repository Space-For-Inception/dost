from twilio.rest import Client 
 
account_sid = 'AC91f82bcbaa098fc043cdd757e3a718d1' 
auth_token = '3099c149a3b641ab65bacf9c7497287d'
client = Client(account_sid, auth_token) 

def sendMessage(clientPhoneNo:str = '+917798044008', msg:str = 'Hello World'):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body =msg,      
                                to   =f'whatsapp:{clientPhoneNo}' 
                            )

if __name__ == "__main__":
    cool = "C"+"O"*8+"L"
    for i in range(10):
        sendMessage(msg=f"*{cool[i]}*")