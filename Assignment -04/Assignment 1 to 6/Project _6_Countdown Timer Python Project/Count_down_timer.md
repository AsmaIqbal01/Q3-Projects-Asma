```python
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Timer completed!')

def main():
    print('Count down Timer!')
    while True:
        try:
            t = int(input('Enter the time in seconds: '))
            if t < 0:
                print("Please enter a positive integer.")
            else:
                countdown(t)
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
```

    Count down Timer!
    Enter the time in seconds: 5
    Timer completed!
    
