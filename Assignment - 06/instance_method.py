class Dog:
    def __init__(self,name,breed):
        self.name =name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! ")

if __name__=="__main__":
    dog = Dog("Buddy","Golder Retriever")
    dog.bark()