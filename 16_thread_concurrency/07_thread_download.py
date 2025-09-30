import threading
import requests
import time

def download_file(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished download from {url}, size: {len(response.content)} bytes")

urls = [
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/webp"
]

start = time.time()
threads = []

for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")