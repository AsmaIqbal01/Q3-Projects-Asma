```python
from IPython.display import display, HTML
def main():
  print("00_count_nums")
  user_numbers = get_user_numbers()
  num_dict = count_nums(user_numbers)
  print_counts(num_dict)

def get_user_numbers():
  user_numbers=[]
  while True:
    user_input=input("Enter a number or press Enter to finish :")
    if user_input == "":
      break
    try:
      num = int(user_input)
      user_numbers.append(num)
      display(HTML(f"<span style='color :blue;'>{num}</span>"))
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
  return user_numbers

def count_nums(num_list):
  num_dict = {}
  for num in num_list:
    if num in num_dict:
      num_dict[num] += 1
    else:
      num_dict[num] = 1
  return num_dict

def print_counts(num_dict):
  for num in num_dict:
    print(f"{num} appears {num_dict[num]} times.")

if __name__=='__main__':
  main()
```

    00_count_nums
    Enter a number or press Enter to finish :12
    


<span style='color :blue;'>12</span>


    Enter a number or press Enter to finish :12
    


<span style='color :blue;'>12</span>


    Enter a number or press Enter to finish :344
    


<span style='color :blue;'>344</span>


    Enter a number or press Enter to finish :43
    


<span style='color :blue;'>43</span>


    Enter a number or press Enter to finish :32
    


<span style='color :blue;'>32</span>


    Enter a number or press Enter to finish :
    12 appears 2 times.
    344 appears 1 times.
    43 appears 1 times.
    32 appears 1 times.
    
