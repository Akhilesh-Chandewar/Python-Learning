import threading
import time

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)  # Simulate time taken to boil milk
    print("Milk boiled.")

def toast_bread():
    print("Toasting bread...")
    time.sleep(3)  # Simulate time taken to toast bread
    print("Bread toasted.")

start = time.time()
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bread)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")