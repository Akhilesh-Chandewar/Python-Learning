from multiprocessing import Process, current_process
import time


def cpu_heavy_task():
    print(f"Process {current_process().name} starting CPU-heavy task")
    count = 0
    for i in range(10**7):
        count += i
    print(
        f"Process {current_process().name} finished CPU-heavy task with count {count}"
    )


if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy_task) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
