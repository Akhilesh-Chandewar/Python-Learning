class OutOfIngredientsError(Exception):
    def __init__(self, message):
        self.message = message

def make_chai(milk , sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Out of ingredients")
    else:
        print("Chai is ready")

make_chai(0 , 0)
