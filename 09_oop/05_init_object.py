class ChaiOrder:
    def __init__(self , type_ , size , sugar):
        self.type = type_
        self.size = size
        self.sugar = sugar
    
    def summary(self):
        return f"Type: {self.type} , Size: {self.size} , Sugar: {self.sugar}"
    
order_1 = ChaiOrder("masala chai" , "small" , 2)
print(order_1.summary())

order_2 = ChaiOrder("ginger chai" , "large" , 3)
print(order_2.summary())

