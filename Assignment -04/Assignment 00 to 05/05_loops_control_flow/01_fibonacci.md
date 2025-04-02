```python
MAX_VALUE = 10000

def main():
    print("01_fibonacci")
    curr_term = 0
    next_term = 1
    index = 0  # Initialize an index to keep track of the term number

    while curr_term <= MAX_VALUE:
        print(f"f({index}) => {curr_term}")  # Print the term in the desired format
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
        index += 1  # Increment the index for the next term

if __name__ == "__main__":
    main()
```

    01_fibonacci
    f(0) => 0
    f(1) => 1
    f(2) => 1
    f(3) => 2
    f(4) => 3
    f(5) => 5
    f(6) => 8
    f(7) => 13
    f(8) => 21
    f(9) => 34
    f(10) => 55
    f(11) => 89
    f(12) => 144
    f(13) => 233
    f(14) => 377
    f(15) => 610
    f(16) => 987
    f(17) => 1597
    f(18) => 2584
    f(19) => 4181
    f(20) => 6765
    
