# import arrow

# brewing_time = arrow.utcnow()
# print(f"brewing time {brewing_time.to('Europe/Rome')}")


from collections import namedtuple

chai_recipe = namedtuple('chai_recipe' , 'base liquid')
chai_order = chai_recipe('tea leaves' , 'water')
print(f"chai order {chai_order}")

a = 5
b = 5
print(id(a) == id(b))

print(True or False)