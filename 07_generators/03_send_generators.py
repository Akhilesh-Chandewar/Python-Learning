def chai_customer():
    print('What chai do you like ?')
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall)
stall.send('masala chai')
stall.send('green tea')