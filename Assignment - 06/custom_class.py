class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is an iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Example usage:
if __name__ == "__main__":
    for number in Countdown(5):
        print(number)
