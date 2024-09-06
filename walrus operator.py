foods = list()

# while True:
#     food = input("What food do u like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
#
# print(foods)

while (food := input("what food do you like? :")) != "quit":
    foods.append(food)

print(foods)