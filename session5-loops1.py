l = [10, 20, 30, 40, 50]

sum = 0
for value in l:
    print(value)
    sum = sum + value
    
print(sum)

for value in range(5,10):
    print(value)

for value in range(10, 100, 5):
    print(value)
    
for value in range(5):
    print(value)

for value in range(10):
    print(value)
    
l = [10, 20, 30, 40, 50, 60]
key = 400

for value in l:
    if value == key:
        print("Element found")
        break
    else:
        pass
        print("Statement after continue statement")
else:
    print("Element not found")
    
print("Statement after the for loop")

for index, value in enumerate(l):
    print(index, value)

