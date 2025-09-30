import threading
import time

def cpu_heavy_task():
    print(f"Thread {threading.current_thread().name} starting CPU-heavy task")
    count = 0
    for i in range(10**7):
        count += i
    print(f"Thread {threading.current_thread().name} finished CPU-heavy task with count {count}")

start = time.time()
threads = [threading.Thread(target=cpu_heavy_task) for _ in range(7)]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")