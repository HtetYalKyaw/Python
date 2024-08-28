# def upper_everything(elements: list[str]) -> list[str]:
#     return [element.upper() for element in elements]
#
#
# loud_list: list[str] = upper_everything(['mario', 'Luigi', 'peach'])
#
#
# print(loud_list)

# -----------------------------------------------------------------------------------------------------------------------------

people: list[str] = ['John', 'Charlotte', 'Macloving', 'Mark', 'Keith']

# Llist: list[str] = []
#
# for p in people[:]:
#     if len(p) > 7:
#         Llist.append(p)
#         people.remove(p)

Llist: list[str] = [p for p in people if len(p) > 7]
people: list[str] = [p for p in people if len(p) <= 7]

print(f'Llist :{Llist}')
print(f'people : {people}')
