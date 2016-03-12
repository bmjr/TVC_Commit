



def checkForLists(trello,board):
	foundTodo = False
	foundinprog= False
	foundsubmitted=False
	founddone= False

	lists = trello.boards.get_list(board)
	for item in lists:
		if item['name']=="TODO":
			foundTodo=True
		elif item['name']=="In-Progress":
			foundinprog=True
		elif item['name']=="Submitted":
			foundsubmitted= True
		elif item['name']=="Done":
			founddone=True
	if(foundTodo == False):
		trello.boards.new_list(board,"TODO")
	if(foundinprog==False):
		trello.boards.new_list(board,"In-Progress")
	if(foundsubmitted ==False):
		trello.boards.new_list(board,"Submitted")
	if(founddone ==False):
		trello.boards.new_list(board,"Done")
	


def getDoneList(trello,board):
	found = False
	ID =""
	lists = trello.boards.get_list(board)
	for item in lists:
		if item['name']=="Done":
			ID = item['id']
			found=True
	if(found ==False):
		trello.boards.new_list(board,"Done")
		lists = trello.boards.get_list(board)
		for item in lists:
			if item['name']=="Done":
				ID = item['id']

	return ID


def getTODOList(trello,board):
	found = False
	ID =""	
	lists = trello.boards.get_list(board)
	for item in lists:
		if item['name']=="TODO":
			ID = item['id']
			found=True
	if(found==False):
		trello.boards.new_list(board,"TODO")
		lists = trello.boards.get_list(board)
		for item in lists:
			if item['name']=="TODO":
				ID = item['id']

	return ID


def getSubmittedList(trello,board):
	found = False
	ID =""
	lists = trello.boards.get_list(board)
	for item in lists:
		if item['name']=="Submitted":
			ID = item['id']
			found=True
	if(found== False):
		trello.boards.new_list(board,"Submitted")
		lists = trello.boards.get_list(board)
		for item in lists:
			if item['name']=="Submitted":
				ID = item['id']

	return ID

def getInProgList(trello,board):
	found = False
	ID =""
	lists = trello.boards.get_list(board)
	for item in lists:
		if item['name']=="In-Progress":
			ID = item['id']
			found=True
	if(found == False):
		trello.boards.new_list(board,"In-Progress")
		lists = trello.boards.get_list(board)
		for item in lists:
			if item['name']=="In-Progress":
				ID = item['id']

	return ID








