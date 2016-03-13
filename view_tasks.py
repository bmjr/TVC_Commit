

def viewTasks(trello, board):
	lists = trello.boards.get_list(board)
	count = 0
	for item in lists:
		print("{} {}".format(count, item['name']))
		count = count +1

	view = int(raw_input("Which list would you like to view? "))
	viewlist = trello.lists.get_card(lists[view]['id'])
	for item in viewlist:
		print("{} {}".format(item['name'],item["desc"]))