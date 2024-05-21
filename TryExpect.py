try:
    numerator = int(input("Enter a number to be divided : "))
    denominator = int(input("Enter a number to divided : "))

    result = numerator / denominator


except ZeroDivisionError as e:
    print(e)
    print("Cant be divided by zero!")
except ValueError as e:
    print(e)
    print("!!Enter Numer only plz!!")
except Exception as e:
    print(e)
    print("Error!")
else:
    print(result)
finally:
    print("This will always execute")