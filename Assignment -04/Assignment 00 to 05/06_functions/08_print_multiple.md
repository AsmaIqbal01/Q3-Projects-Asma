```python
from IPython.display import display, HTML

def print_multiple(message:str, repeat:int):
  for i in range(repeat):
    print(message)
def main():
  print("08_print_multiple")
  message = str(input("Enter any message: "))
  repeat=int(input("How many times to repeat a message: "))
  display(HTML(f"<style>body {{ color: blue; }}print_multiple(message,repeat)</style>"))
  display(HTML(f"<style>body {{ color: blue; }}print_multiple('{message}',{repeat})</style>"))
  print_multiple(message,repeat)
if __name__=='__main__':
  main()
```

    08_print_multiple
    Enter any message: hello
    How many times to repeat a message: 6
    


<style>body { color: blue; }print_multiple(message,repeat)</style>



<style>body { color: blue; }print_multiple('hello',6)</style>


    hello
    hello
    hello
    hello
    hello
    hello
    
