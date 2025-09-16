class BaseChai:
    def __init__(self , type_):
        self.type = type

    def prepare(self):
        print("Preparing chai" , self.type)

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices to chai")

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("masala chai")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

    
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()