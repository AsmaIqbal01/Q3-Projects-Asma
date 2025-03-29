```python
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb
def main():
  print("07_tiny_mad_lib")
  print("MAD LIBS---FUN WORD GAME!")
  adjective:str=input("Please type an adjective and press enter. ")
  noun:str=input("Please type a noun and press enter.")
  verb:str=input("Please type a verb and press enter.")
  print(f"{SENTENCE_START}{adjective} {noun} {verb}")
if __name__=='__main__':
  main()
```

    07_tiny_mad_lib
    MAD LIBS---FUN WORD GAME!
    Please type an adjective and press enter. tiny
    Please type a noun and press enter.plant
    Please type a verb and press enter.fly
    Panaversity is fun. I learned to program and used Python to make my tiny plant fly
    
