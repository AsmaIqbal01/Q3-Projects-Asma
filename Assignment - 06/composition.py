class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

    def start_engine(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine
    
    def start(self):
        print(f"Starting the {self.brand}.")
        self.engine.start_engine()

if __name__ == "__main__":
    my_engine = Engine(250)
    my_car = Car("Toyota",my_engine)
    my_car.start()