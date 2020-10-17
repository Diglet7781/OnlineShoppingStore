#Online Shopping Center
import sys

from modules.GUI import GUI
from modules.Customer import Customer
from modules.Account import Account
from modules.Inventory import *
from modules.Cart import Cart


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
        print("Here is the current items available: \n")
        c_cart = Cart()
        Inv = Inventory()

        user_item = input("Please enter the item you would like to buy:")

        Inventory.item_verify(c_cart,Inv.get_itemDB(), user_item)

    else:
        print("Invalid Credentials")
        print("Please, try again later!")
        exit_input = input('')
        if exit_input:
            exit(0)

        # GUI.showOptions()
        # option = input("Enter option: ")
        # if int(option) == 3:
        #     GUI.loginCredential = []
        #     print("Logout")
        #     sys.exit()


main()
