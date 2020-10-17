#Online Shopping Center
from modules.GUI import GUI
from modules.Customer import Customer
from modules.Account import Account

def main():

    #Display mainWindow
    GUI.showMainWindow()
    GUI.displayEmptyLines(1)

    #Display LoginWindow
    GUI.showLoginWindow()


    #instantiate account object
    account = Account()

    #set up login credentials
    account.username = GUI.loginCredentials[0]["username"].strip()
    account.password = GUI.loginCredentials[0]["password"].strip()

    account.login()
    if account.login():
        GUI.displayEmptyLines(1)
        print(f"Welcome to OSC {account.firstName} {account.lastName} ")
    else:
        print("Invalid Credentials")
        print("Please, try again later!")

main()
