# Datatypes:

# 1 Int : Immutable data type
num1 = 100
print(type(num1))


# 2 Float: Immutable data type
num2 = 15.25
print(type(num2))


print(id(num1))
num1 = 105
print(id(num1))


# 3 str '' " " """ """ : Immutable data type
s = "'Python' sample string"
print(id(s))
print(s, type(s))

s = "new value"
print(id(s))


# 4 list : [] : Mutable data type
l = [10, 20, 30, 40, 50, "Python", "Django"]
print(id(l))
l.append(60)
print(l)
print(id(l))


# 5 Tuple : Immutable data type
t = (10, 20, 30)


# 6 Dict : Mutable data type
d = {"name":"ABC", "email":"abc@gmail.com"}


# 7 Set {} : Mutable data type 
s = {10, 20, 30, 40}


# 8 bool : True False 


# 9 complex : 4 + 3j


help(str)