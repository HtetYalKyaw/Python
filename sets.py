utensils = {"fork","spoon","knife"}
foods ={"pasta","spaghetti", "meatball"}
foods.add("cake")
utensils.remove("fork")
utensils.update(foods)

dinner_table = utensils.union(foods)

for x in dinner_table:
    print(x)
