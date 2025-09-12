chai_order = dict(type="masala chai" , size="small" , sugar=2)
print(f"chai order {chai_order}")

chai_recipe = {}
chai_recipe['base'] = 'tea leaves'
chai_recipe['liquid'] = 'water'
print(f"chai recipe {chai_recipe}")
print(f"base of chai {chai_recipe['base']}")
print(f"liquid of chai {chai_recipe['liquid']}")

del chai_recipe['liquid']
print(f"chai recipe {chai_recipe}")

print(f"is sugar in order {'sugar' in chai_order}")

print(f"keys of chai order {list(chai_order.keys())}")
print(f"values of chai order {list(chai_order.values())}")
print(f"items of chai order {list(chai_order.items())}")

last_item = chai_order.popitem()
print(f"Removed item {last_item}")

extra_spices = {'cardamon' : 'crushed' , 'ginger' : 'sliced'}

chai_recipe.update(extra_spices)
print(f"updated chai recipe {chai_recipe}")

chai_note = chai_order.get('note' , 'no note')
print(f"chai note {chai_note}")

