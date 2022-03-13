x = eval('10**2')
print(x)

print(eval('sum([10, 20, 30, 40, 50])'))

i = 10
print(eval('i*50'))

x = 10
y = 5

print(eval('x ** y', {'x': x, 'y': y}))     # globally

print(eval('x - y', {}, {'x': 50, 'y': 100}))   # with locals
