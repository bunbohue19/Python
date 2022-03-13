def newOrder(**kwargs):
    print(kwargs)

newOrder(Tea = "Green", price = 1.8, size = "medium")

def newOrder2(**kwargs):
    for key, value in kwargs.items():
        print("{} is equal to {}".format(key, value))

newOrder2(Tea = "Green", price = 1.8, size = "medium", sugar = True)