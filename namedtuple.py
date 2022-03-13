from collections import namedtuple

Point_2d = namedtuple('Point_2D', ['x', 'y'])
new_point = Point_2d(50, 100)
print(new_point)
print(isinstance(new_point, Point_2d))
print(isinstance(new_point, tuple))

#   unpatching tuple
x, y = new_point
print(f'{x}, {y}')

#   index numbers
x = new_point[0]
y = new_point[1]
print(f'{x}, {y}')

#   Iterate over new point
for item in new_point:
    print(item)
    
new_circle = namedtuple('new_circle', 'center_x, center_y, _radius', rename=True)
print(new_circle._fields)
