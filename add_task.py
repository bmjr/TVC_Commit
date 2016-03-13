import checkLists

def newTask(trello, boardID):
	listId = checkLists.getTODOList(trello,boardID)
	name = str(raw_input("Name of card: "))
	name = name +" [" +str(raw_input("Please add a branch name: "))+"]"
	description = str(raw_input("desc of card:\n"))
	trello.cards.new(name,listId,description)
	raw_input("Card Added. Press Enter to Continue")