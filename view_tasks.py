import checkout_branch
import checkLists
import PrintTest
import start_task

def viewTasks(trello, board):
	lists = trello.boards.get_list(board)
	count = 0

	while True:
		count = 0
		for item in lists:
			print("{} {}".format(count, item['name']))
			count = count +1

		view = int(raw_input("\nWhich list would you like to view? "))
		print
		viewlist = trello.lists.get_card(lists[view]['id'])

		count = 0
		for card in viewlist:
			card['index'] = count
			card['branchName'] = checkout_branch.getBranchName(card['name'])
			card['due'] = start_task.generateDateString(str(card['due']))
			card['dateLastActivity'] = start_task.generateDateString(str(card['dateLastActivity']))
			count = count + 1
		
		fmt = [
		('INDEX', 'index', 10),
	    ('CARD NAME', 'name', 30),
	    ('BRANCH NAME', 'branchName', 20),
	    ('DESCRIPTION', 'desc', 60),
	    ('DUE DATE', 'due', 20),
	    ('LAST EDIT', 'dateLastActivity', 20)
		]

		print(PrintTest.TablePrinter(fmt, ul='=')(viewlist))

		y = str(raw_input("\nFinished viewing lists (y/n): "))
		print
		if y.lower() =="y" :
			break