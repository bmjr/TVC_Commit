def newTask(trello, boardID):
	listsJson = trello.boards.get_list(boardID)
	for item in listsJson:
		if item['name'].lower() == "tasks to do": 
			print("List Found")
			listId = item['id']
			break
	name = str(raw_input("Name of card: "))
	description = str(raw_input("desc of card:\n"))
	trello.cards.new(name,listId,description)