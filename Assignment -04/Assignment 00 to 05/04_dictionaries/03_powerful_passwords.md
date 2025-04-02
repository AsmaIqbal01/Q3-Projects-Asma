```python
from hashlib import sha256  # Import the sha256 hashing function from the hashlib library

def login(email, stored_logins, password_to_check):
    """
    Check if the provided email and password match the stored credentials.

    Parameters:
    email (str): The email of the user trying to log in.
    stored_logins (dict): A dictionary containing email-password pairs where passwords are hashed.
    password_to_check (str): The password entered by the user.

    Returns:
    bool: True if the email exists and the password matches, False otherwise.
    """
    # Check if the hashed version of the provided password matches the stored hash for the email
    if stored_logins[email] == hash_password(password_to_check):
        return True  # Login successful
    return False  # Login failed

def hash_password(password):
    """
    Hash a password using SHA-256.

    Parameters:
    password (str): The password to be hashed.

    Returns:
    str: The hexadecimal representation of the hashed password.
    """
    # Encode the password to bytes and hash it using SHA-256, then return the hex digest
    return sha256(password.encode()).hexdigest()

def main():
    print("03_powerful_passwords")  # Print the title of the program

    # Dictionary to store email-password pairs, where passwords are stored as hashed values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # Hash of "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Hash of "karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # Hash of "123!456789"
    }

    # Test login attempts with various email-password combinations
    print(login("example@gmail.com", stored_logins, "word"))  # Should return False (wrong password)
    print(login("example@gmail.com", stored_logins, "password"))  # Should return True (correct password)

    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Should return True (correct password)
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Should return True (correct password)

    print(login("student@stanford.edu", stored_logins, "password"))  # Should return False (wrong password)
    print(login("student@stanford.edu", stored_logins, "123!456789"))  # Should return True (correct password)

if __name__ == '__main__':
    main()  # Execute the main function when the script is run
```

    03_powerful_passwords
    False
    True
    True
    True
    False
    False
    
