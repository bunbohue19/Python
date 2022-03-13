from math import *

exec("print('Hi, there!')")

new_code = '''x = 10
y = 20
print('x + y =', x + y)'''
exec(new_code)

insert_code = input('Enter Python code here: ')
exec(insert_code)

exec('print(abs(-10))')

exec('print(dir())')

code = '''x = sqrt(16)
print(x)'''

exec(code, {'sqrt': sqrt})
# or exec(code)