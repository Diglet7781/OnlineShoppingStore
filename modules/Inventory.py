import json
from modules.Cart import *

class Inventory:
    def __init__(self):
        inventory = open("Database/Inventory.json")
        items = json.load(inventory)
        items_list = []

        for item in items['items']:
            items_list.append((item['item'], item['item_description'], item['item_id'],item['price'], item['Quantity']) )

        self.items_list = items_list

    def get_ItemList(self):

        return self.items_list

    def showInventory(current_Inventory):

        item_list = current_Inventory.get_ItemList()

        for item in range(len(item_list)):
            print ("Item: ", item_list[item][0])
            print ("Description: ", item_list[item][1])
            print ("Price: ", item_list[item][3])
            print ("Quantity: ", item_list[item][4])
            print("\n")

    def item_verify(Curr_cart, current_Inventory, user_item, user_quantity):

        item_list = current_Inventory.get_ItemList()

        for item in range(len(item_list)):

            if item_list[item][0].lower() == user_item.lower().strip():

                if user_quantity <= item_list[item][4]:
                            Cart.addToCart(Curr_cart, item_list[item][0], user_quantity, item_list[item][3])
                            print ("Added to Cart successfully")
                            break
        else:
            print("Item does not exist, please retry\n")

    def updateQuantity(current_Inventory, cart):

        item_list = current_Inventory.get_ItemList()

        for item in range(len(cart)):
        
            if item_list[item][0] == cart[item][0]:


                item_list[item][4] = item_list[item][4] - cart[item][1]
