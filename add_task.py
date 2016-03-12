def newTask(trello, boardID):
    lists = trello.boards.get_list(boardID)
    print(lists)
