users = [
    {"id": 1, "total": 100, "coupon": "qwer45"},
    {"id": 2, "total": 200, "coupon": "qwer46"},
    {"id": 3, "total": 500, "coupon": "dewfsd"},
]

discounts = {
    "qwer45": (0.2 , 0),
    "qwer46": (0.3 , 0),
    "dewfsd": (0 , 10)
}

for user in users:
    perc , fixed = discounts.get(user["coupon"] , (0 , 0))
    discount = user["total"] * perc + fixed
    user["total"] -= discount

print(users)
