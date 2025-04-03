```python
def access_elem(lst,index):
  try:
    return lst[index]
  except IndexError:
    return "Index out of range."
def modify_elem(lst,index,new_value):
  try:
    lst[index]=new_value
    return lst
  except IndexError:
    return "Index out of range."
def slice_list(lst,start,end):
  try:
    return lst[start:end]
  except IndexError:
    return "Invalid indices."

def index_game():
  print("Index Game")
  my_list = [42, "Hello", 3.14, "Python", 100]
  print("Current List", my_list)
  print("Choose an operation: access, modify or slice ")
  operation=input("Enter operation ")
  if operation == 'access':
    index=int(input("Enter index "))
    print(access_elem(my_list,index))
  elif operation == 'modify':
    index=int(input("Enter index "))
    new_value=input("Enter new value ")
    print(modify_elem(my_list,index,new_value))
  elif operation == 'slice':
    start=int(input("Enter start index "))
    end=int(input("Enter end index "))
    print(slice_list(my_list,start,end))
  else:
    print("Invalid operation")
if __name__=='__main__':
  index_game()

```

    Index Game
    Current List [42, 'Hello', 3.14, 'Python', 100]
    Choose an operation: access, modify or slice 
    Enter operation access
    Enter index2
    3.14
    
