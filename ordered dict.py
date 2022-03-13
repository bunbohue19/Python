from collections import OrderedDict
# Create dict

new_dict = {'apple': 3, "banana": 7, "cherry": 4}
print(new_dict)

# empty ordered dict
new_ordereddict = OrderedDict()
print(new_ordereddict)

# ordered dict from regular
new_ordereddict = OrderedDict(new_dict)
print(new_ordereddict)

# add item to dictionary
new_ordereddict['fig'] = 5
print(new_ordereddict)

# replace item in a dict
new_ordereddict['apple'] = 10
print(new_ordereddict)

# delete values
new_ordereddict.pop('cherry')
print(new_ordereddict)

# move to end
new_ordereddict.move_to_end('apple')
print(new_ordereddict)

# reverse iteration
for item in reversed(new_ordereddict):
    print(item)


