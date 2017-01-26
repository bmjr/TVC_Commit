import PrintTest

def viewLists(trello, board):
	lists = trello.boards.get_list(board)
	for item in lists:
		print(item['name'])

def viewCards(trello, board, a):
	l = None
	
	if "-l" in a:
		try:
			index = a.index("-l")
			l = a[index+1]
		except Exception as e:
			print(e)
			print("Error parsing arguments")
			return
	else:
		print("lists:\n")
		viewLists(trello,board)
		l = raw_input("list to view cards from:\t")
		
	lists = trello.boards.get_list(board)
	lst = None
	for item in lists:
		if item['name'] == l :
			lst = item
			break
			
	if lst is None:
		print("Unable to find list of matching name")
		return	

	viewlist = trello.lists.get_card(lst['id'])

	for card in viewlist:
		card['dateLastActivity'] = generateDateString(str(card['dateLastActivity']))
		
	fmt = [
	('CARD NAME','name', 40),
	('DESCRIPTION','desc',100),
	('LAST EDIT', 'dateLastActivity',20)
	]
	print(PrintTest.TablePrinter(fmt, ul='=')(viewlist))
		
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
