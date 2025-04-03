```python
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Start with letters (both uppercase and lowercase)

    if use_digits:
        characters += string.digits  # Add digits if requested (0-9)
    if use_special:
        characters += string.punctuation  # Add special characters if requested (!,.,?,/,-,_,+,=)

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Password Generator")
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter password length (6-16): "))
            if 6 <= length <= 16:
                break
            else:
                print("Please enter a length between 6 and 16.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user preferences for digits and special characters
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate the password
    password = generate_password(length, use_digits, use_special)
    print(f"Generated Password: `{password}`")

if __name__ == '__main__':
    main()
```

    Password Generator
    Enter password length (6-16): 7
    Include digits? (y/n): y
    Include special characters? (y/n): y
    Generated Password: `dEZ}_]'`
    
