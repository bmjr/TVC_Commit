import checkLists

def reviewTask(trello,board):
	listid = checkLists.getSubmittedList(trello,board)
	cards = trello.lists.get_card(listid)
	count =0
	for item in cards:
		print("{} {}".format(count,item['name']))
		count = count +1

	indexSelected = int(raw_input("Select card to review: "))
	cardId= cards[indexSelected]['id']
	while (True):
		ans = str(raw_input("Accept submitted solution [y/n]: "))
		if ans.lower() == "y":		
			doneId = checkLists.getDoneList(trello,board)	
			trello.cards.update_idList(cardId, doneId)
			break
		elif ans.lower()== "n":
			progId = checkLists.getInProgList(trello,board)	
			trello.cards.update_idList(cardId, progId)
			reason = str(raw_input("Reason for rejection:\n"))
			reason = "Submit request rejected, due to: " + reason
			trello.cards.new_action_comment(cardId,reason)
			break
	
