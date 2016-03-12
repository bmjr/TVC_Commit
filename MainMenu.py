import shell_engine
import add_task
from trello import TrelloApi

appKey = "bbe4f72dcc11de483fec87b87db05532"


def view():
    print("view")


def add():
    print("add")
    add_task.newTask(init(), getBoard())


def start():
    print("start")


def submit():
    print("submit")


def review():
    print("review")


def init():
    tr = TrelloApi(appKey)
    print("Please visit the following website and copy the key:")
    print('https://trello.com/1/authorize?key=' + appKey +
          '&name=TVC_Commit&expiration=30days&response_type=token&scope=read,write')
    trelloToken = str(raw_input("Please enter key: "))
    tr.set_token(trelloToken)
    return tr


def getBoard():
    boardID = str(raw_input("Please enter board id: "))
    return boardID

options = {
    1: view,
    2: add,
    3: start,
    4: submit,
    5: review,
}

if __name__ == '__main__':

    print("""
    Welcome to the TVC main menu
    ============================
    1 - View Tasks in To do
    2 - Add Task"
    3 - Start Task"
    4 - Submit Task"
    5 - Review Task"
    ============================
    """)
    choice = int(raw_input("Please Enter Your Choice: "))
    shell_engine.runShellCommand("clear")
    options[choice]()