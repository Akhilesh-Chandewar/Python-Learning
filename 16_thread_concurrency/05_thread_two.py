import threading
import time

def prepare_chai(type_ , wait_time):
    print(f"Preparing {type_} chai...")
    time.sleep(wait_time)  # Simulate time taken to prepare chai
    print(f"{type_} chai is ready.")

t1 = threading.Thread(target=prepare_chai, args=("Masala", 4))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 2))
t1.start()
t2.start()
t1.join()
t2.join()
print("Both types of chai are ready.")