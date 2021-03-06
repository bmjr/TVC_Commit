from trello import TrelloApi
import urllib
appKey = "bbe4f72dcc11de483fec87b87db05532"
trelloToken =""


def setUpAuth():
    trello = TrelloApi(appKey)
    while True :
        try:
            print("Please visit the following website and copy the key:")
            print('https://trello.com/1/authorize?key=' + appKey +
              '&name=TVC_Commit&expiration=30days&response_type=token&scope=read,write')
            trelloToken = str(raw_input("Please enter key:\n"))
            trello.set_token(trelloToken)
            trello.tokens.get(trelloToken)

            break
        except Exception as e:
            print(e)
            print("Key Incorrect.\n\n")

    file = open('Token', mode="w")
    file.write(trelloToken)
    file.close()
    
    return trello


def checkAuth(trello,board):
    trello.tokens.get(trello._token)


def getnamepass():
    name = input("Please Enter Your username:\n")
    psswrd = input("Please Enter Your Password:\n")
    return [name, psswrd]
