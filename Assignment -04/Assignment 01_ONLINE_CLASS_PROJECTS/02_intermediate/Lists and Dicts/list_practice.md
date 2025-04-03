```python
def main():
  print("List Practice----Problem-1")
  fruits_lst=['apple', 'banana', 'orange', 'grape', 'pineapple']
  print("Length of the list:", len(fruits_lst))
  for i in range(len(fruits_lst)):
    print(f"{i+1}. {fruits_lst[i]}")
  fruits_lst.append('mango')
  print("Updated Fruit List: ",fruits_lst)
if __name__ == '__main__':
  main()
```

    List Practice----Problem-1
    Length of the list: 5
    1. apple
    2. banana
    3. orange
    4. grape
    5. pineapple
    Updated Fruit List:  ['apple', 'banana', 'orange', 'grape', 'pineapple', 'mango']
    
