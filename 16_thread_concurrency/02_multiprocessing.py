from multiprocessing import Process
from time import sleep

def brew_chai(name):
    print(f"Brewing chai for {name}")
    sleep(3)
    print(f"Chai brewed for {name}")

if __name__ == "__main__":
    chai_makers = [
        Process(target = brew_chai , args = (f"Chai maker #{i}" ,)) for i in range(1 , 4)
    ]
    for p in chai_makers:
        p.start()
    for p in chai_makers:
        p.join()
    print(f"All chai is brewed!")