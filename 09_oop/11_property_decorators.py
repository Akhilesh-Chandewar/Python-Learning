class TeaLeaf:
    def __init__(self , age):
        self.age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self , age):
        if 1<= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be between 1 and 5")
    
    @age.getter
    def age(self):
        return self._age

leaf = TeaLeaf(3)
print(leaf.age)

leaf.age = 4
print(leaf.age)

# leaf.age = 6
# print(leaf.age)