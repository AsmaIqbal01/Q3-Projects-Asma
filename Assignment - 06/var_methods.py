class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(f"The {self.brand} car has started.")

my_car=Car("Toyota")
print(my_car.brand)
my_car.start()