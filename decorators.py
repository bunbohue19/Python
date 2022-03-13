def adding(num):
    return num + 1

adding_one = adding 
print(adding_one(10))
print(adding_one(20)) 

def adding(num):
    def adding_one(num):
        return num + 1
    
    total = adding_one(num)
    return total

def calling(new_func):
    new_number = 10
    return new_func(new_number)

print(calling(adding))

# return a function from a function
def hello():
    def greeting():
        return "Hi there"
    return greeting

new_greet = hello()
print(new_greet())


# Closure
def new_message(text):
    "Outer message"
    def another_message():
        "Our nested message"
        print(text)
    another_message()

new_message("Hello, this is a random text message")

def new_capital(new_func):
    def new_inner():
        the_func = new_func()
        upper_case = the_func.upper()
        return upper_case
    
    return new_inner

def greeting():
    return "Hi, Python Programming"

new_decorating = new_capital(greeting)

print(new_decorating())

# The same as
@new_capital

def greeting():
    return "Hi, Python Ptogramming"

print(greeting())




















