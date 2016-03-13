import checkout_branch
import checkLists
import PrintTest


def startTask(trello,boardID):
	listID = checkLists.getTODOList(trello,boardID)
	toDoCards = trello.lists.get_card(listID)

	count = 0
	for card in toDoCards:
		card['index'] = count
		card['branchName'] = checkout_branch.getBranchName(card['name'])
		card['due'] = generateDateString(str(card['due']))
		card['dateLastActivity'] = generateDateString(str(card['dateLastActivity']))
		count = count + 1
	
	fmt = [
	('INDEX', 'index', 30),
    ('CARD NAME', 'name', 30),
    ('BRANCH NAME', 'branchName', 20),
    ('DESCRIPTION', 'desc', 60),
    ('DUE DATE', 'due', 20),
    ('LAST EDIT', 'dateLastActivity', 20)
	]

	print(PrintTest.TablePrinter(fmt, ul='=')(toDoCards))

	
		
	indexSelected = int(raw_input("Select the card index: "))
	selectedCard = toDoCards[indexSelected]['name']
	cardId = toDoCards[indexSelected]['id']
	startId = checkLists.getInProgList(trello,boardID)
	trello.cards.update_idList(cardId, startId)
	branchName = str(checkout_branch.getBranchName(selectedCard))
	checkout_branch.createBranch(branchName)


def generateDateString(string):
	if string != "None":
		unparsedDueDate = str(string).split("T")
		parsedDueDate = unparsedDueDate[0]
		parsedDueTime = unparsedDueDate[1]
		parsedDueTimeArray = parsedDueTime.split(":")
		timeString = parsedDueTimeArray[0] + ":" + parsedDueTimeArray[1]

		parsedDueDateArray = parsedDueDate.split("-")
		parsedDueDateArray.reverse()

		dueDateString = ""
		for dateElement in parsedDueDateArray:
			if dueDateString == "":
				dueDateString = dateElement
			else:
				dueDateString = dueDateString + "/" + dateElement
		dueDateString = timeString + " " + dueDateString
	else:
		dueDateString = "Not set"

	return dueDateString
