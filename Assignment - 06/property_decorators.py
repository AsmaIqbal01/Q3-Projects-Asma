class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Get the price of the product."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price of the product."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price of the product."""
        print("Deleting price...")
        del self._price

# Example usage:
if __name__ == "__main__":
    p = Product(100)
    print(f"Initial Price: {p.price}")  # Get price

    p.price = 150  # Set a new price
    print(f"Updated Price: {p.price}")

    del p.price  # Delete the price attribute
    # Accessing after deletion will raise an AttributeError
    try:
        print(p.price)
    except AttributeError as e:
        print(f"Error: {e}")
