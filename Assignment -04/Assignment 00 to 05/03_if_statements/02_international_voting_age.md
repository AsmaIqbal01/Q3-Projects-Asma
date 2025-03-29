```python
PETETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():
    print("02_international_voting_age")
    user_age: int = int(input("Enter your age: "))

    # Check eligibility for PETETURKSBOUIPO
    if user_age >= PETETURKSBOUIPO_AGE:
        print("You are eligible to vote in PETETURKSBOUIPO.")
    else:
        print("You are not eligible to vote in PETETURKSBOUIPO where voting age is " + str(PETETURKSBOUIPO_AGE) + ".")

    # Check eligibility for STANLAU
    if user_age >= STANLAU_AGE:
        print("You are eligible to vote in STANLAU.")
    else:
        print("You are not eligible to vote in STANLAU where voting age is " + str(STANLAU_AGE) + ".")

    # Check eligibility for MAYENGUA
    if user_age >= MAYENGUA_AGE:
        print("You are eligible to vote in MAYENGUA.")
    else:
        print("You are not eligible to vote in MAYENGUA where voting age is " + str(MAYENGUA_AGE) + ".")

if __name__ == '__main__':
    main()
```

    02_international_voting_age
    Enter your age: 40
    You are eligible to vote in PETETURKSBOUIPO.
    You are eligible to vote in STANLAU.
    You are not eligible to vote in MAYENGUA where voting age is 48.
    
