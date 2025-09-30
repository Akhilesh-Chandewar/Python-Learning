import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)  # Simulate a blocking I/O operation
    return f"{item} is in stock!"

async def main():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        res = await loop.run_in_executor(pool, check_stock, "masala chai")
        print(res)

asyncio.run(main())