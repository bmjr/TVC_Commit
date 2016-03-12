import userpass
from trello import TrelloApi
from trello import boards

def newTask(trello, boardID):
    lists = trello.boards.get_list(boardID)
    print(lists)