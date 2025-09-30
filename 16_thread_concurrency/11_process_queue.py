from multiprocessing import Process, Queue 
def prepare_queue():
    quque.put("Masala chai is ready!")


if __name__ == "__main__":
    quque = Queue()
    process = Process(target=prepare_queue)
    process.start()
    process.join()
    print(quque.get())