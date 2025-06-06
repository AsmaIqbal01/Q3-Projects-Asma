def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage:
if __name__ == "__main__":
    p = Person("Alice")
    print(p.greet())  # Output: Hello from Decorator!
