names = ["Ahmed", "Ibra", "Joe", "Marcelo"]

new_enum = enumerate(names)
print(type(new_enum))

new_list = list(new_enum)
print(new_list)

# Change start position
new_enum = enumerate(names, start = 10)

new_list = list(new_enum)
print(new_list)

for index, name in enumerate(names):
    print(index, name)
    
names = ["Ahmed", "Ibra", "Joe", "Marcelo"]
new_enum = enumerate(names)
print(new_enum.__next__())
print(new_enum.__next__())
print(new_enum.__next__())
print(new_enum.__next__())
