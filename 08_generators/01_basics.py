def serve_chai():
    yield "Masala chai"
    yield "Green tea"
    yield "Lemon tea"
    yield "Mint tea"

for chai in serve_chai():
    print(chai)

def get_chai_list():
    return ["Masala chai" , "Green tea" , "Lemon tea" , "Mint tea"]

# genrator functions
def get_chai_gen():
    yield "Masala chai"
    yield "Green tea"
    yield "Lemon tea"
    yield "Mint tea"

chai = get_chai_gen()
# print(*chai)
print(next(chai))