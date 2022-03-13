numbers = [10, 20, 30, 40, 50, 60, 70]

new_iterator = iter(numbers)

print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))

seq = "Iterator tutorial in python"

new_iterator = iter(seq)
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))

def new_iterator(n):
    my_iterable = iter(n)
    
    while True:
        try:
            print(next(my_iterable))
        except StopIteration:
            break
        
new_iterator([10, 30, 50, 70])
new_iterator((11, 12, 13, 14, 15))
new_iterator("A powerful iterator function!")

# Building Iterator using OOP
class Incrementing:
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if self.count <= 15:
            x = self.count
            self.count = self.count + 1
            return x
        else: 
            raise StopIteration

new_obj = Incrementing()
new_iter = iter(new_obj)

print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))

for num in Incrementing():
    print(num)
    
