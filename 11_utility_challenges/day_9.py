import time
import os

while True:
    try:
        seconds = int(input("Enter the time in seconds: "))
        if seconds < 1:
            print("Time must be greater than 0.")
            continue
        break  # ✅ exit loop if valid input
    except ValueError:
        print("Please enter a valid number.")

print("\n⏳ Timer started...")
for remainder in range(seconds, 0, -1):
    mins, secs = divmod(remainder, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(f"Time remaining: {timer}", end="\r")
    time.sleep(1)

print("\n⏰ Time's up!!")

# Beep sound options
print("\a")  # ASCII bell (works in most Ubuntu terminals)

# If you want a real beep sound (requires beep package installed)
# os.system("beep -f 1000 -l 500")
