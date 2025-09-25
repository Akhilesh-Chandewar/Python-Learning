from multiprocessing import Process
import time

def crunch_number():
    print(f"Starting crunch number")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Finished crunch number")

if __name__ == "__main__":
    start = time.time()
    p1 = Process(target = crunch_number)
    p2 = Process(target = crunch_number)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(f"Time taken: {end - start} secs")