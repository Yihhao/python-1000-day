def add(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 3, 5))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


car = Car(make="Auto")
print(car.make)