```python
def main():
  print("07_get_list")
  lst=[]
  elem=input("Enter elements in a list: ")
  while elem:
    lst.append(elem)
    elem=input("Enter next element: ")
  print("Here is the complete list: ", lst)
if __name__=='__main__':
  main()

```

    07_get_list
    Enter elements in a list: apple
    Enter next element: orange
    Enter next element: lemon
    Enter next element: strawberry
    Enter next element: chery
    Enter next element: 
    Here is the complete list:  ['apple', 'orange', 'lemon', 'strawberry', 'chery']
    
