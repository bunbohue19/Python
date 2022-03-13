from collections import Counter

new_list = ['a', 'b', 'c', 'a', 'b', 'b', 'a', 'c', 'b']
print(Counter(new_list))

# Counter with string

new_string = "Welcome to advanced foundations"
print(Counter(new_string))

# Counter with list

new_list = ['a', 'b', 'c', 'a', 'b', 'b', 'a', 'c', 'b', 'd']
print(Counter(new_list))

# Counter with dictionary

new_dictionary = {'a': 1, "b": 2, "c": 3, "d": 4, "d": 4}
print(Counter(new_dictionary))

# Counter with tuple

new_tuple = ('apple', 'banana', 'cherry', 'apple', 'apple', 'banana', 'fig', 'cherry')
print(Counter(new_tuple))

# empty Counter

_counting = Counter()
print(_counting)
_counting.update("Hi, Python is fun!")
print(_counting)

# delete from Counter

new_dict = {'a': 1, "b": 2, "c": 3, "d": 4, "d": 4}
del new_dict["d"]
print(Counter(new_dict))










