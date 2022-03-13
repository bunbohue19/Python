# Regular way
fruits_list = ["fig", "banana", "kiwi", "cherry"]
my_list = []

for item in fruits_list:
    if "i" in item:
        my_list.append(item)
        
print(my_list)



# Use list comprehension
fruits_list = ["fig", "banana", "kiwi", "cherry"]
my_list = [item for item in fruits_list if "c" in item]

print(my_list)

# Iterate over sequence with regular way
new_list = []       # empty list

for new_char in "Power of comprehension":
    new_list.append(new_char)
    
print(new_list)     # printing the list

# The same as
new_list = [new_char for new_char in "Power of comprehension"]
print(new_list)     # printing the list

# You can use nested list comprehension
new_matrix = []
for x in range(5):
    new_matrix.append([])       # adding empty sublist inside the list
    
    for y in range(8):
        new_matrix[x].append(y)

print(new_matrix)

