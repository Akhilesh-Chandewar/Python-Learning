sugar_amount = 2
print(f"The sugar amount is {sugar_amount} grams.")

#number are immutable, so this creates a new integer object and reassigns the variable
sugar_amount = 3
print(f"The sugar amount is now {sugar_amount} grams.")

print(f"id of sugar_amount: {id(sugar_amount)}")
print(f"id of 2: {id(2)}")
print(f"id of 3: {id(3)}")