from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock(): 
            counter.value += 1
    print("Final counter value:", counter.value)

if __name__ == "__main__":
    counter = Value("i", 0)
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print("Counter after all processes:", counter.value)

