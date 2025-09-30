import threading

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # only one lock, not nested
            counter += 1


threads = [threading.Thread(target=increment_counter) for _ in range(5)]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Final counter:", counter)
