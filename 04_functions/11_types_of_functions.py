total_chai = 0

def pure_chai(cups):
    return cups * 10

# not recomonded
def impure_chai(cups):
    global total_chai
    total_chai += cups
    return cups

def pour_chai(n):
    print(n)
    if n==0:
        return "All cups poured"
    return pour_chai(n-1)
print(pour_chai(5))

chai_types = ["green tea" , "black tea" , "chai wala" , "masala chai" , "ginger chai"]
filter_chai = list(filter(lambda chai_type : "chai" in chai_type , chai_types))
print(filter_chai)

map_chai = map(lambda chai_type : chai_type.upper() , chai_types)
print(*map_chai)