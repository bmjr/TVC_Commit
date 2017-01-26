from trello import TrelloApi

def listBoards(trello):
	boardsJson = trello.members.get_board("me")
	print("\nBoards:\n")
	if len(boardsJson) == 0:
		print("No Boards Created\n")
		return;
	for item in boardsJson:
			print(item['name'])


def changeBoard(trello, boardName):
	boardsJson = trello.members.get_board("me")	
	boardId = ""
	if len(boardsJson) == 0:
		print("No Boards Created\n")
		return;
	for item in boardsJson:
		if item['name'].lower() == boardName.lower(): 
			print("Board Found")
			boardId = item['id']
			print("changed to board : " +boardName )
			break 
	if boardId != "":
		f = open('Token',mode ="w")
		f.write(trello._token+"," + boardId)
		return boardId
	print("board Not found")
	return None
		
	
