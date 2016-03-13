import checkLists
import shell_engine

def submitTask(trello,board):
	listid = checkLists.getInProgList(trello,board)
	cards = trello.lists.get_card(listid)
	count =0
	for item in cards:
		print("{} {}".format(count,item['name']))
		count = count +1

	indexSelected = int(raw_input("Select card to submit: "))
	cardId= cards[indexSelected]['id']
	submitId = checkLists.getSubmittedList(trello,board)	
	trello.cards.update_idList(cardId, submitId)
	comment= str(raw_input("Comment for final Commit: "))
	cmd = "git commit -a -m " + "'"+comment+"'"
	print (cmd)
	shell_engine.runShellCommand(cmd)
	trello.cards.new_action_comment(cardId,cmd)


