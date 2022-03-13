from itertools import zip_longest as l1

for i in zip([1, 2, 3], ['x', 'y', 'z']):
    print(i)
    
x = set(zip())
print(x)

for item in zip([10, 20, 30]):
    print(item)
    
for item in zip([10, 20, 30], ['x', 'y', 'z'], ['$', '@', '#']):
    print(item)


x = set(zip([10, 20], [30, 40, 50, 60]))
print(x)

x = set(l1([10, 20], [30, 40, 50, 60]))
print(x)

# unzipping values
unzipping = zip([10, 20, 30], ['x', 'y', 'z'], ['$', '@', '#'])
x, y, z = zip(*unzipping)
print(x, y, z)

