import shell_engine

def view():
    print("view")
def add():
    print("add")
def start():
    print("start")
def submit():
    print("submit")
def review():
    print("review")

options ={
    1 : view,
    2 : add,
    3 : start,
    4 : submit,
    5 : review,
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
    choice = input("Please Enter Your Choice: ")
    shell_engine.runShellCommand("clear")
    options[choice]()

