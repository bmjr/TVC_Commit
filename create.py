import urllib
import lists
import time

def createList(trello, board, name):
	trello.boards.new_list(board, name)
	print("new List create "+ name)
	return
	
	
	
def createCard(trello, board , listname):
	ls = trello.boards.get_list(board)
	ID = ""
	for item in ls:
		if item['name'] == listname:
			ID = item['id']
	
	if ID == "":
		print("List "+ str(listname) + " not found.")
		return 
	print("list found")
	cardName = raw_input("Please Enter card name: ")
	if cardName.isspace() == True:
		print("Name cannot be blank.")
		return
		
	addDesc = raw_input("Do you want to add Description> y/n")
	desc = None
	if addDesc == "y" or addDesc == "yes":
		desc = raw_input("\ndescription: \n")
	
	trello.cards.new(cardName, ID, desc)
	print("\nCard created")
	
	time.sleep(1)
	lists.viewCards(trello, board, ["-l", listname])
	
