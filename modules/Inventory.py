import json
from modules.Cart import *

class Inventory:
    def __init__(self):
        inventory = open("Database/Inventory.json")
        items = json.load(inventory)
        self.items = items

        for item in items['items']:
            print (item['item'])
            print (item['item_description'])
            print (item['price'],"$")
            print ("Quantity: ",item['Quantity'],"\n")

    def item_verify(curr_cart, itemDB, user_item):

        for item in itemDB['items']:

            if item['item'].lower() == user_item.strip().lower():
                # Decrease Quantity
                current_quanity = item['Quantity']
                quantity = input("How many would you like: ")

                if quantity <= current_quanity and quantity > "0":

                    Cart.addToCart(curr_cart.get_cart(),item['item'], quantity, item['price'])
                    Inventory.update_Remove_inventory(itemDB,item, quantity)
                    new_user_item = input("Please enter another item you would like to buy (if none press any Enter to continue):")
                    if new_user_item == '':
                        Cart.ShowCart(curr_cart.get_cart())
                        remove_item = input("Enter the item you would like to remove from your cart?")
                        n_quantity = input("How many would you like to remove?")
                        Inventory.update_ADD_inventory(itemDB,remove_item, n_quantity, curr_cart.get_cart())
                        while(remove_item != ''):
                            Cart.ShowCart(curr_cart.get_cart())
                            remove_item = input("Enter the another item you would like to remove from your cart?(if none press Enter to continue)")
                            if remove_item != '':
                                n_quantity = input("How many would you like to remove?")
                                Inventory.update_ADD_inventory(itemDB,remove_item, n_quantity, curr_cart.get_cart())

                        #Remove Cart --> Finalize Cart --> Payment
                    Inventory.item_verify(curr_cart, itemDB, new_user_item)
                else:
                    print ("Currently your selected quantity is over/below the limit, only a max of", item['Quantity'], "can be bought")
                    print ("Please Retry")
                    Inventory.item_verify(curr_cart,itemDB, user_item)



    def get_itemDB(self):
        item_DB = self.items
        return item_DB

    def update_Remove_inventory(itemDB, item, quantity):
        inventory = open("Database/Inventory.json", "w")
        item['Quantity'] = str(int(item['Quantity']) - int(quantity))
        json.dump(itemDB, inventory)
        inventory.close()

    def update_ADD_inventory(itemDB, item, quantity, curr_cart):
        inventory = open("Database/Inventory.json", "w")
        item['Quantity'] = str(int(item['Quantity']) + int(quantity))
        json.dump(itemDB, inventory)
        inventory.close()
        curr_cart[item][1] = str(int(item['Quantity']) + int(quantity))
