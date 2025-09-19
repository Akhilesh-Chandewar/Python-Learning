
def calculate_age(age):
    DAYS_IN_YEARS = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    age_in_days = age * DAYS_IN_YEARS
    age_in_hours = age_in_days * HOURS_IN_DAY
    age_in_minutes = age_in_hours * MINUTES_IN_HOUR
    return round(age_in_days), round(age_in_hours), round(age_in_minutes)

while True:
    try:
        age = int(input("Enter your age: "))
        days, hours, minutes = calculate_age(age)
        print(f"You are {age} years old. That's {days} days, {hours} hours, and {minutes} minutes.")
        
        again = input("Would you like to try again? (y/n): ").strip().lower()
        if again != "y":
            print("Good bye")
            break

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        