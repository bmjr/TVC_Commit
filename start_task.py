import checkout_branch
import checkLists
import PrintTest

def startTask(trello,boardID):
	listID = checkLists.getTODOList(trello,boardID)
	toDoCards = trello.lists.get_card(listID)

	
	fmt = [
    ('card name', 'name', 11),
    ('description', 'desc', 20),
    ('Last edited', 'dateLastActivity', 20)
	]

	print(PrintTest.TablePrinter(fmt, ul='-')(toDoCards))

	count = 0
	for card in toDoCards:
		print( "{} {}".format(count,card['name'])) #count+" "+card['name'])
		count = count + 1
		
	indexSelected = int(raw_input("Select the card number: "))
	selectedCard = toDoCards[indexSelected]['name']
	branchName = str(checkout_branch.getBranchName(selectedCard))
	checkout_branch.createBranch(branchName)