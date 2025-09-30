import threading
import time

def monitor():
    while True:
        print("Monitoring...")
        time.sleep(1)

thread = threading.Thread(target=monitor, daemon=True)
thread.start()

