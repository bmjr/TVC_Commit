from trello import TrelloApi
import json
import userpass
import checkLists
	
def setup(trello):
	trello = userpass.setUpAuth()
	while(True):
		boardsJson = trello.members.get_board("me")
		if boards.length == 0:
			print("No Boards Created\n")
			break;
			
		print ("Choose a start board:\n")
		for item in boardsJson:
			print(item['name'] +"\n")
		board = str(raw_input("Which board would you like to use?\n"))
		boardId=""
		for item in boardsJson:
			if item['name'].lower() == board.lower(): 
				print("Board Found")
				boardId = item['id']
				break
		if boardId != "":
			f = open('Token',mode ="w")
			f.write(trello._token+"," + boardId)
			checkLists.checkForLists(trello,boardId)
			return [trello, boardId]
		
		print("sorry board not found. \n\n")
	
	
