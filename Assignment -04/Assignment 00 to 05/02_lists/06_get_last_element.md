```python
def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[len(lst) - 1])


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    print("06_get_last_element")
    lst = get_lst()
    get_last_element(lst)


if __name__ == '__main__':
    main()
```

    06_get_last_element
    Please enter an element of the list or press enter to stop. moon
    Please enter an element of the list or press enter to stop. star
    Please enter an element of the list or press enter to stop. sun
    Please enter an element of the list or press enter to stop. sky
    Please enter an element of the list or press enter to stop. 
    sky
    
