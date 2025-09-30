import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt(data):
    return data[::-1]


async def main():
    loop = asyncio.get_running_loop()
    data = "Hello, World!"

    with ProcessPoolExecutor() as pool:
        encrypted_data = await loop.run_in_executor(pool, encrypt, data)
        print(f"Encrypted data: {encrypted_data}")

if __name__ == "__main__":
    asyncio.run(main())