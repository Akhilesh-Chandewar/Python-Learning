import threading
import time

def take_order():
    for i in range(1 , 4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

order_thread = threading.Thread(target = take_order)
brew_thred = threading.Thread(target = brew_chai)

order_thread.start()
brew_thred.start()

order_thread.join()
brew_thred.join()

print(f"All orders are served!")