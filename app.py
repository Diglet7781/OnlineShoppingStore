#Online Shopping Center
import sys

from modules.GUI import *
from modules.Customer import *
from modules.Account import *
from modules.Inventory import *
from modules.Cart import *
from modules.purchase import *

def options(option, Curr_cart, current_user, account):

    Curr_Inv = Inventory()
    if option == 1:

        Inventory.showInventory(Curr_Inv)

        user_item = input("Enter an item you would like to add to your cart: ")
        user_quantity = input("How many would you like: ")
        Inventory.item_verify(Curr_cart, Curr_Inv, user_item, user_quantity)

        while(1):

            user_item = input("Enter an item you would like to add to your cart(if no more items are needed just press Enter to continue): ")
            if user_item == '':
                GUI.showOptions()
                option = int(input("Enter option: "))
                print("\n")
                options(option, Curr_cart, current_user, account)
                break
            user_quantity = input("How many would you like: ")
            Inventory.item_verify(Curr_cart, Curr_Inv, user_item, user_quantity)

    elif option == 2:
        Cart.showCart(Curr_cart)
        while(1):

            remove_item = input("If you need to remove an item please enter it(if your cart is good just press Enter to continue): ")
            if remove_item == '' and len(Curr_cart.get_cart()) > 0:
                print ("\n")
                print ("\n")
                Cart.showCart(Curr_cart)
                address = input("Please enter your address: ")
                OSC_card = input("Please input your 10 digit OSC Card: ")
                confrim = input("Are you sure you want to purchase what is in your cart?(Y/N)")
                if "Y":
                    p = Purchase(current_user,Curr_cart.get_cart(), address, OSC_card)
                    Inventory.updateQuantity(Curr_Inv, Curr_cart.get_cart())
                    print ("Purchase Complete")
                    Curr_cart = Cart()
                    GUI.showOptions()
                    print("Purchase History: ", p.get_order_History())
                    option = int(input("Enter option: "))
                    print("\n")
                    options(option, Curr_cart, current_user, account)
                    break
                if "N":
                    GUI.showOptions()
                    option = int(input("Enter option: "))
                    print("\n")
                    options(option, Curr_cart, current_user, account)
                    break
            else:
                GUI.showOptions()
                option = int(input("Enter option: "))
                print("\n")
                options(option, Curr_cart, current_user, account)
            remove_quantity = input("How many would you like to remove: ")
            Cart.removeQuantity(Curr_cart, remove_item, remove_quantity)

    elif option == 4:
        GUI.loginCredential = []
        account.logout()

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
    current_user = account.username

    account.login()
    if account.login():
        Curr_cart = Cart()
        GUI.displayEmptyLines(1)
        print(f"Welcome to OSC {account.firstName} {account.lastName} ")
        GUI.showOptions()
        option = int(input("Enter option: "))
        print("\n")
        options(option, Curr_cart, current_user, account)

    else:
        print("Invalid Credentials")
        print("Please, try again later!")
        exit_input = input('')
        if exit_input:
            exit(0)

main()
