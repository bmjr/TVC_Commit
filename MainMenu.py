import shell_engine
import add_task
import start_task
import submit_task
import userpass
from trello import TrelloApi

appKey = "bbe4f72dcc11de483fec87b87db05532"


def view():
    print("view")


def add():
    print("add")
    initArray = init()
    add_task.newTask(initArray[0], initArray[1])


def start():
    print("start")
    initArray = init()
    start_task.startTask(initArray[0], initArray[1])


def submit():
    print("submit")
    initArray = init()
    submit_task.submitTask(initArray[0], initArray[1])


def review():
    print("review")


def init():
	trello = TrelloApi(userpass.appKey)
	file = open('Token', mode="r")
	trelloDetails = file.readline().split(",")
	file.close()
	trello.set_token(trelloDetails[0])
	return [trello,trelloDetails[1]]


def getBoard():
    boardID = str(raw_input("Please enter board id: "))
    return boardID

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
    while True:
        print("""
        Welcome to the TVC main menu
        ============================
        1 - View Tasks in To do
        2 - Add Task
        3 - Start Task
        4 - Submit Task
        5 - Review Task
        ============================
        """)
        choice = int(raw_input("Please Enter Your Choice: "))
        shell_engine.runShellCommand("clear")
        options[choice]()
