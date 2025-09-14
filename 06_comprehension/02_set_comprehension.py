favourite_chais = ["masala chai" , "ginger chai" , "iced lemon chai" , "iced mint chai" , "elaichi chai"]
unique_chais = {chai for chai in favourite_chais}
print(unique_chais)

recipes = {
    "masala chai" : ["ginger" , "cardamom" , "clove"],
    "elaichi chai" : ["cardamom" , "milk"],
    "spicy chai" : ["ginger" , "cardamom" , "clove" , "black pepper"]
}

unique_spices = {______ for ingredients in recipes.values() for ______ in ingredients}
print(unique_spices)