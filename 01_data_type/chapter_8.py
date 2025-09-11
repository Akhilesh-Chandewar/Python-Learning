# list is mutable
ingredient = ["water" , "milk" , "tea leaves"]

ingredient.append("sugar")
print(f"ingredients are {ingredient}")

ingredient.remove("milk")
print(f"ingredients are {ingredient}")

spices_options = ["ginger" , "cadamom"]
chai_ingredient = ["water" , "milk"]

chai_ingredient.extend(spices_options)
print(f"chai ingredients are {chai_ingredient}")

chai_ingredient.insert(2 , "tea leaves")
print(f"chai ingredients are {chai_ingredient}")

last_added = chai_ingredient.pop()
print(f"last added {last_added}")
print(f"chai {chai_ingredient}")

print(f"index of tea leaves {chai_ingredient.index('tea leaves')}")

print(f"count of tea leaves {chai_ingredient.count('tea leaves')}")

chai_ingredient.reverse()
print(f"chai ingredients are {chai_ingredient}")

chai_ingredient.sort()
print(f"chai ingredients are {chai_ingredient}")

chai_ingredient.clear()
print(f"chai ingredients are {chai_ingredient}")

sugar_level = [1,2,3,4,5]
print(f"Total sugar level {sum(sugar_level)}")
print(f"Minimum sugar level {min(sugar_level)}")
print(f"Maximum sugar level {max(sugar_level)}")

base_liquid = ["water" , "milk"]
extra_flavour = ["ginger" , "cinnamon"]

# operator overloading
full_liquid_mix = base_liquid + extra_flavour 
print(f"full liquid mix {full_liquid_mix}")

strong_brew = ["tea leves" , "ginger"] * 3
print(f"strong brew {strong_brew}")

raw_spices = bytearray(b"CINNAMON")
print(f"raw spices {raw_spices}")

raw_spices = raw_spices.replace(b"CINNA", b"CARDA")
print(f"raw spices {raw_spices}")
