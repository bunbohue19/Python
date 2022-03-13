# 1
for number in range(1500 - 1, 2700 + 1):
    if (number % 7 == 0) & (number % 5 == 0):
        print(number)

# 2
even = 0
odd = 0
for number in range(10):
    if (number % 2 == 0):
       even += 1
    else:
       odd += 1
       
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)

# 3
for number in range(0, 51):
    if (number % 3 == 0):
        if (number % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif (number % 5 == 0):
        if (number % 3 == 0):
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(number)
        
        
# 4
numbers = [16, 188, 321, 99, 45, 24]
sum = 0
for number in numbers:
    sum += number
        
average = sum / len(numbers)
print(sum, average)

# 5
number = int(input('Enter an integer'))
if number == 0:
    print("0! = 1")
else:
    factorial = 1
    for item in range(1, number + 1):
        factorial *= item
    print(factorial)
