def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Chai stall is closed")

stall = chai_stall()
next(stall)
stall.send("masala chai")
stall.send("ginger chai")
stall.close()
