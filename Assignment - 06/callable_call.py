class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initialize the multiplication factor

    def __call__(self, value):
        return value * self.factor  # Multiply input by the factor

# Example usage:
if __name__ == "__main__":
    multiplier_instance = Multiplier(3)

    # Test if instance is callable
    print(callable(multiplier_instance))  # Expected output: True

    # Call instance like a function
    result = multiplier_instance(10)
    print(result)  # Expected output: 30
