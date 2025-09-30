import asyncio
import threading
import time

def bg_worker():
    while True:
        time.sleep(1)
        print("Logging the system status...")

async def fetch_order():
    await asyncio.sleep(2)
    print("Order fetched")

threading.Thread(target=bg_worker, daemon=True).start()
asyncio.run(fetch_order())