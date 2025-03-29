```python
from IPython.display import display,Markdown
def add_three_copies(my_list,data):
  for i in range(3):
    my_list.append(data)
def main():
  print("04_flowing_with_data_structures")
  message = input("Enter a message to copy: ")
  my_list=[]
  display(Markdown(f"List before : **_{my_list}_**"))
  add_three_copies(my_list,message)
  display(Markdown(f"List after : **_{my_list}_**"))

if __name__=='__main__':
  main()

```

    04_flowing_with_data_structures
    Enter a message to copy: Hello World!
    


List before : **_[]_**



List after : **_['Hello World!', 'Hello World!', 'Hello World!']_**

