import asyncio

async def brew_coffee():
    print("Starting to brew coffee...")
    await asyncio.sleep(2) 
    print("Coffee is ready!")
    return "Coffee"

asyncio.run(brew_coffee())