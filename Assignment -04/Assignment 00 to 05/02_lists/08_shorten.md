```python
MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():

    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    print("08_shorten")
    lst = get_lst()
    shorten(lst)
    print("The final remaining list is",lst)

if __name__ == '__main__':
    main()
```

    08_shorten
    Please enter an element of the list or press enter to stop. potato
    Please enter an element of the list or press enter to stop. tomato
    Please enter an element of the list or press enter to stop. cucumber
    Please enter an element of the list or press enter to stop. capsicum
    Please enter an element of the list or press enter to stop. chilli
    Please enter an element of the list or press enter to stop. zucchini
    Please enter an element of the list or press enter to stop. broccli
    Please enter an element of the list or press enter to stop. brinjal
    Please enter an element of the list or press enter to stop. cauliflower
    Please enter an element of the list or press enter to stop. 
    cauliflower
    brinjal
    broccli
    zucchini
    chilli
    capsicum
    The final remaining list is ['potato', 'tomato', 'cucumber']
    
