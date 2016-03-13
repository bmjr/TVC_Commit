import checkout_branch
import checkLists

def startTask(trello,boardID):
	listID = checkLists.getTODOList(trello,boardID)
	toDoCards = trello.lists.get_card(listID)

	count = 0
	for card in toDoCards:
		print( "{} {}".format(count,card['name'])) #count+" "+card['name'])
		count = count + 1
		
	indexSelected = int(raw_input("Select the card number: "))
	selectedCard = toDoCards[indexSelected]['name']
	branchName = str(checkout_branch.getBranchName(selectedCard))
	checkout_branch.createBranch(branchName)