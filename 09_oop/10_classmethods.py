class ChaiOrder:
    def __init__(self , type_ , size , sugar):
        self.type = type_
        self.size = size
        self.sugar = sugar

    @classmethod
    def from_dict(cls , order_dict):
        return cls(order_dict['type'] , order_dict['size'] , order_dict['sugar'])
    
    @classmethod
    def from_string(cls , order_string):
        tea_type , size , sugar = order_string.split(',')
        return cls(tea_type , size , sugar)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ['small' , 'medium' , 'large']
    
print(ChaiUtils.is_valid_size('small'))
    
order_1 = ChaiOrder.from_dict({'type' : 'ginger chai' , 'size' : 'large' , 'sugar' : 2})
print(order_1.__dict__)

order_2 = ChaiOrder.from_string('ginger chai , large , 2')
print(order_2.__dict__)

order_3 = ChaiOrder('ginger chai' , 'large' , 2)
print(order_3.__dict__)