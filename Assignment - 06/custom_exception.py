class InvalidAgeError(Exception):
    """Custom exception raised when age is invalid (less than 18)."""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is not allowed. Age must be at least 18.")

# Example usage:
if __name__ == "__main__":
    try:
        age_to_check = 16
        check_age(age_to_check)
        print("Age is valid.")
    except InvalidAgeError as e:
        print(f"InvalidAgeError caught: {e}")

