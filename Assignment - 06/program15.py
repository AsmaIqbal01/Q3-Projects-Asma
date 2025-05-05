class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")

class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C):
    pass  # No override, inherits from B and C

# Example usage:
if __name__ == "__main__":
    d = D()
    d.show()  # Which show() is called depends on MRO

    # Print the MRO of class D
    print("Method Resolution Order for class D:")
    for cls in D.__mro__:
        print(cls)
