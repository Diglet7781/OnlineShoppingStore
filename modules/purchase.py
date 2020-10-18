
class Purchase:
    def __init__(self, user, cart, address, OSC_card):
        self.user = user
        self.cart = cart
        self.address = address
        self.OSC_card = OSC_card

        His_cart = cart

        total_price = 0
        for item in range(len(cart)):
            total_price += cart[item][2]

        self.total_price = total_price

        Order_History = [(user, His_cart, address, OSC_card, total_price)]
        self.order_history = Order_History

    def get_order_History(self):
        order_history = self.order_history
        return order_history
