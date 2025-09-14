chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Elaichi"
    kitchen()
    print(f"Outside fucntion {chai_type}")

front_desk()
print(f"Final outside fucntion {chai_type}")