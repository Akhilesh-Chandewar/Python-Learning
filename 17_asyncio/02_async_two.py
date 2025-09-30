import asyncio


async def brew(name, delay):
    print(f"Starting to brew {name}...")
    await asyncio.sleep(delay)
    print(f"{name} is ready!")
    return name


async def main():
    await asyncio.gather(brew("Espresso", 2), brew("Latte", 3), brew("Cappuccino", 1))

asyncio.run(main())
