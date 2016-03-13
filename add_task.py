import checkLists

def newTask(trello, boardID):
	listId = checkLists.getTODOList(trello,boardID)
	name = str(raw_input("Name of card: "))
	description = str(raw_input("desc of card:\n"))
	trello.cards.new(name,listId,description)