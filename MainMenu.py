import shell_engine
import add_task
import start_task
import submit_task
import review_task
import userpass
import view_tasks
import sys
import os.path
import FirstTimeUse
from trello import TrelloApi

appKey = "bbe4f72dcc11de483fec87b87db05532"
trello = TrelloApi(appKey)
boardID= ""


def view():  
	view_tasks.viewTasks(trello, boardID)

def add():
    add_task.newTask(trello, boardID)


def start():
    start_task.startTask(trello, boardID)


def submit():
    submit_task.submitTask(trello, boardID)


def review():
    review_task.reviewTask(trello, boardID)


def init():
    if os.path.isfile("Token") ==False:
        FirstTimeUse.main()
    global trello
    trello = TrelloApi(userpass.appKey)
    file = open('Token', mode="r")
    trelloDetails = file.readline().split(",")
    file.close()
    trello.set_token(trelloDetails[0])
    global boardID
    boardID = trelloDetails[1]
    return [trello,trelloDetails[1]]

def exit():
    sys.exit(0)

options = {
    1: view,
    2: add,
    3: start,
    4: submit,
    5: review,
    6: exit
}

if __name__ == '__main__':
    init()
    while True:
        shell_engine.runClearCommand()
        print("""

	Welcome to the TVC main menu
	============================
	1 - View Tasks in To do
	2 - Add Task
	3 - Start Task
	4 - Submit Task
	5 - Review Task
	6 - exit
	============================
		""")
        choice = int(raw_input("Please Enter Your Choice: "))
        options[choice]()