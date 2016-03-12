from trello import TrelloApi
import json
import userpass
boardId=""


def main():
	
	trello = userpass.setUpAuth()

	while(True):
		board = input("Which board would you like to use?\n")
		boardsJson = trello.members.get_board("me")
		boardId=""
		for item in boardsJson:
			if item['name'].lower() == board.lower(): 
				print("Board Found")
				boardId = item['id']
				break
		if boardId != "":
			break

	f = open('Token',"a")
	f.write("\n" + boardId)

	return [trello,boardId]
	

if __name__ == '__main__':
	main()



