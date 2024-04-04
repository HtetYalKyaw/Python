# slicing = create a substring by extracting elements from another string indexing [] or slice []
#           [start : stop : step]

# name = "Htet Yal"
#
# first_name = name[:4]             [0:4]
# last_name = name[5:]              [5:end]
# funky_name = name[::3]            [0:end:3]
# reversed_name = name[::-1]        [0:end:-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

website1 = "https://google.com"
website2 = "https://amazon.com"
slice = slice(8,-4)

print(website1[slice])
print(website2[slice])