def add(*stuff):
    sum = 0
    stuff = list(stuff)
    for i in stuff:
        sum += i
    return sum

print(add(2,5,6,8,11))