import checkLists
import checkout_branch
import shell_engine

def reviewTask(trello,board):
	listid = checkLists.getSubmittedList(trello,board)
	cards = trello.lists.get_card(listid)
	count =0
	for item in cards:
		print("{} {}".format(count,item['name']))
		count = count +1

	indexSelected = int(raw_input("Select card to review: "))
	cardId= cards[indexSelected]['id']
	cardBranchName = checkout_branch.getBranchName(cards[indexSelected]['name'])
	while (True):
		ans = str(raw_input("Accept submitted solution [y/n]: "))
		if ans.lower() == "y":		
			doneId = checkLists.getDoneList(trello,board)	
			trello.cards.update_idList(cardId, doneId)
			shell_engine.runShellCommand("git checkout master")
			shell_engine.runShellCommand("git merge " + cardBranchName)
			shell_engine.runShellCommand("git push")
			shell_engine.runShellCommand("git branch -D " + cardBranchName)
			shell_engine.runShellCommand("git push origin :"+cardBranchName)
			break
		elif ans.lower()== "n":
			progId = checkLists.getInProgList(trello,board)	
			trello.cards.update_idList(cardId, progId)
			reason = str(raw_input("Reason for rejection:\n"))
			reason = "Submit request rejected, due to: " + reason
			trello.cards.new_action_comment(cardId,reason)
			break
	
