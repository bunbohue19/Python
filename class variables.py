# class variables are the variables that are
# declared inside the class

class Flower:
    total_flowers = 10          # class variables
    pass

red = Flower()
white = Flower()

red.count = 15
red.price = 100 

white.count = 12
white.price = 150
white.day = "Monday"

print(red.count, white.day)
print(Flower.total_flowers)
print(red.total_flowers)

white.total_flowers = 20
print(white.total_flowers)

print(Flower.total_flowers)
