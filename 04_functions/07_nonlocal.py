def update_order():
    chai_type = "Elaichi"
    def kichen():
        nonlocal chai_type
        chai_type = "Ginger"
        print(f"Inside fucntion {chai_type}")
    kichen()
    print(f"Outside fucntion {chai_type}")

update_order()