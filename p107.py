class A:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart
    
    def __len__(self):
        return len(self.cart)

a = A('ali', [1,2,3,4,5,6,7,8,9])
len(a)