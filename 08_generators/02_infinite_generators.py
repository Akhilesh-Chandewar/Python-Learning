def infinite_chai_gen():
    count = 0
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai_gen()
user2 = infinite_chai_gen()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))