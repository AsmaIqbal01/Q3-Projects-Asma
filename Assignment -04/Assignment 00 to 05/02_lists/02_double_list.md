```python
def main():
  print('02_double_list')
  numbers:list[int]=[1,2,3,4,5]
  print("Before doubled the numbers : ", numbers)
  for i in range(len(numbers)):
    elem_at_index=numbers[i]
    numbers[i]=elem_at_index*2
  print("After doubled the numbers: ",numbers)
if __name__=='__main__':
  main()
```

    02_double_list
    Before doubled the numbers :  [1, 2, 3, 4, 5]
    After doubled the numbers:  [2, 4, 6, 8, 10]
    
