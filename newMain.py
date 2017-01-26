import shell_engine

import lists
import boards
import setup
import create

import userpass
import view_tasks
import sys
import os.path
import FirstTimeUse
import userpass

from trello import TrelloApi

appKey = "bbe4f72dcc11de483fec87b87db05532"
trello = TrelloApi(appKey)
boardID= ""

def usage():
	print("""Usage :
	./newMain.py commands [options args]*
		- init 					| Runs initial setup.
		- boards				| List all boards
		- checkout				| move to new board
		- lists 				| show all lists on the current board
		- cards -l <listname>	| shows all cards in a list
	""")
	

def changeBoard(a):
	if len(a) == 1:
		print("No board specified")
		return
	print(a[1])
	boardID = boards.changeBoard(trello,a[1])
	
def board(a):
	boards.listBoards(trello)
	
def l(a):
	lists.viewLists(trello, boardID)
	
	
def cards(a):
	if '--help' in a:
		print("""
		Usage :
		cards -l <listname>    	| shows all cards in a list
		""")
		return
	print(a)
	lists.viewCards(trello, boardID, a[1:])
	
def new(a):
	if len(a) ==1 or '--help' in a:
		print("""
		-l 	<listName>		|makes new List
		-c	<listName>		|makes new card, you will be asked after command to provide rest of the details.
		""")
		
	if "-l" in a:
		try:
			create.createList(trello,boardID, a[a.index("-l")+1])
		except Exception as e:
			print(e)
			print("Error command args invalid")	
	if "-c" in a:
		try:
			create.createCard(trello,boardID, a[a.index("-c")+1])
		except Exception as e:
			print(e)
			print("Error command args invalid")			

def init(a):
	print('init')
	setup.setup(trello)

def start():
	if os.path.isfile("Token") == False :
		init()
	
	global trello
	trello = TrelloApi(userpass.appKey)
	file = open('Token', mode="r")
	trelloDetails = file.readline().split(",")
	file.close()
	trello.set_token(trelloDetails[0])
	global boardID
	boardID = trelloDetails[1]
	return [trello,trelloDetails[1]]
    
options = {
	'init': init,
	'boards':board,
	'checkout':changeBoard,
	'lists':l,
	'cards':cards,
	'create':new
}    
    
if __name__ == '__main__':
	start()
	try:
		if len(sys.argv) == 1:
			usage()
		if len(sys.argv) > 1:
			print(sys.argv[1])
			options[sys.argv[1]]( sys.argv[1:])
	except Exception as e:
		print(e)
		print("Error command not recognised.")	





