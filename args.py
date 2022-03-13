def addition(*args):
    result = 0
    for x in args:
        result = result + x
    print(result)
    
addition(10, 20, 30)
addition(1, 2, 3, 4, 5)
