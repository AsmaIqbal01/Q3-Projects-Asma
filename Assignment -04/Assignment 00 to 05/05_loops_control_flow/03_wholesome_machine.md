```python
from IPython.display import display, HTML

AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("03_wholesome_machine")
    print("Please type the following affirmation:")
    print(AFFIRMATION)

    user_feedback = input("Enter your affirmation: ")

    while user_feedback != AFFIRMATION:
        display(HTML(f"<span style='color: blue;'>That's not the affirmation! You entered: {user_feedback}</span>"))
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input("Enter your affirmation: ")

    # Display the confirmation message only after the correct affirmation is entered
    display(HTML(f"<span style='color: blue;'>That's right! You entered: {user_feedback}</span>"))

if __name__ == "__main__":
    main()
```

    03_wholesome_machine
    Please type the following affirmation:
    I am capable of doing anything I put my mind to.
    Enter your affirmation: I am capable
    


<span style='color: blue;'>That's not the affirmation! You entered: I am capable</span>


    Please type the following affirmation: I am capable of doing anything I put my mind to.
    Enter your affirmation: I am capable of doing anything I put my mind to.
    


<span style='color: blue;'>That's right! You entered: I am capable of doing anything I put my mind to.</span>

