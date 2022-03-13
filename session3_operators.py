# Operators in Python
# 1 Arithmetic operators +, -, *, /, //, %, **
# 2 Comparison operators <, >, <=, >=, ==, !=
# 3 Identity Operators is, is not
# 4 Assignment operators =, +=, -=, *=, /=
# 5 Bitwise operators &, |, ^, >>, <<
# 6 Logical operators and, or, not
# 7 Membership operators in, not in

num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 20)

num1 = 100
num2 = 200
print(num1 == num2)
print(num1 > num2)
print(num1 < num2)
print(num1 != num2)

print(num1 is num2)
print(num1 is not num2)

l = [10, 20, 30]
l2 = [10, 20, 30]

print(l == l2)
print(l is l2)
print(l is not l2)
# '==' operator compare the values. On the other hand,
# 'is' operator compare the memory locations. The same for
# identity operator

num1 = num1 + 5
print(num1)
num1 += 5
print(num1)
num1 -= 5
print(num1)

a = 2
b = 1
print(bin(a), bin(b))
print(a & b)
print(a | b)
print(2 >> 1)
print(2 << 1)
print(10 == 10 and 20 == 20)
print(10 == 15 and 20 == 20)
print(10 == 15 or 20 == 20)
print(not(10 == 10))
print(not(10 == 15))

l = [10, 20, 30, 40, 50]
print(30 in l)
print(300 in l)

s = "Python string"
print("Python" in s)
print("Python" not in s)
print("python" in s)
print("python" not in s)



























