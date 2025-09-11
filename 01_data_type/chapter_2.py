spice_mix = set()
print(f"Initial id of spice_mix: {id(spice_mix)}")

#set is mutable, so the id remains the same even after modification
spice_mix.add("cumin")
print(f"Id of spice_mix after adding cumin: {id(spice_mix)}")

spice_mix.add("turmeric")
print(f"Id of spice_mix after adding turmeric: {id(spice_mix)}")