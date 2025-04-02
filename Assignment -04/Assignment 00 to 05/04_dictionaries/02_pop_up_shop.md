```python
from IPython.display import display, Markdown
def main():
  print("02_pop_up_shop")
  fruits={'apple':1.5, 'durian':50, 'jackfruit':80, 'kiwi':1, 'rambutan':1.5, 'mango':5}
  total_cost=0
  for fruit_name in fruits:
    amount_bought = input(f"how many ({fruit_name}) do you want to buy?: ")

    if amount_bought == "":
      break
    try:
      amount_bought = int(amount_bought)
      price = fruits[fruit_name]
      total_cost += (price * amount_bought)
      display(Markdown(f"**_You bought {amount_bought} of {fruit_name}_**"))
    except ValueError:
      print("invalid input")
      continue
  print("total cost is $" + str(total_cost))
if __name__ == "__main__":
  main()

```

    02_pop_up_shop
    how many (apple) do you want to buy?: 4
    


**_You bought 4 of apple_**


    how many (durian) do you want to buy?: 4
    


**_You bought 4 of durian_**


    how many (jackfruit) do you want to buy?: 1
    


**_You bought 1 of jackfruit_**


    how many (kiwi) do you want to buy?: 2
    


**_You bought 2 of kiwi_**


    how many (rambutan) do you want to buy?: 4
    


**_You bought 4 of rambutan_**


    how many (mango) do you want to buy?: 12
    


**_You bought 12 of mango_**


    total cost is $354.0
    
