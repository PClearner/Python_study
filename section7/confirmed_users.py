# test
sandwich_orders = ["apple", "banana", "beef", "sheep", "hot dog"]
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwich.append(sandwich)


sandwich_orders = [
    "apple",
    "banana",
    "pastrami",
    "beef",
    "pastrami",
    "sheep",
    "pastrami",
    "hot dog",
    "pastrami",
]
print("there is no pastrami in this store")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
