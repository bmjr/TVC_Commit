from trello import TrelloApi
import urllib
appKey = "bbe4f72dcc11de483fec87b87db05532"
trelloToken


def setUpAuth():
    trello = TrelloApi(appKey)
    print("Please visit the following website and copy the key:")
    print('https://trello.com/1/authorize?key=' + appKey +
          '&name=TVC_Commit&expiration=30days&response_type=token&scope=read,write')
    trelloToken = input("Please enter key:")
   	with open('token', 'r') as f:
   		f.seek(0)
   		f.truncate()
   		f.write(trelloToken)
    trello.set_token(trelloToken)
    return trello

def getnamepass():

    name = input("Please Enter Your username:\n")
    psswrd = input("Please Enter Your Password:\n")
    return [name, psswrd]
