import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} is brewing chai")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} has brewed chai")

barishta1 = threading.Thread(target = brew_chai , name="Barishta-1")
barishta2 = threading.Thread(target = brew_chai , name="Barishta-2")

start = time.time()
barishta1.start()
barishta2.start()
barishta1.join()
barishta2.join()
end = time.time()
print(f"Time taken: {end - start} secs")