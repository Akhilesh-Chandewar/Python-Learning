essential_species = {"ginger" , "cadamom" , "cinnamon"}
optional_species = {"ginger" , "cloves" , "black pepper"}

#union
all_spices = essential_species | optional_species 
print(f"all spices {all_spices}")

#intersection
common_spices = essential_species & optional_species
print(f"common spices {common_spices}")

#difference
only_essential = essential_species - optional_species
print(f"only essential {only_essential}")

only_optional = optional_species - essential_species
print(f"only optional {only_optional}")

print(f"is cloves in essential {('cloves' in essential_species)}")
print(f"is cloves in optional {('cloves' in optional_species)}")

