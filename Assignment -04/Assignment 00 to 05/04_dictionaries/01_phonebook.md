```python
def read_phone_numbers():
  phonebook= {}
  while True:
    name=input("Enter name: ")
    if name == "":
      break
    number=input("Enter number: ")
    phonebook[name] = number
  return phonebook

def print_phonebook(phonebook):
  print("\n Phonebook: ")
  for name in phonebook:
    print(f" {name} -> {phonebook[name]}")
def lookup_numbers(phonebook):
  while True:
    name=input("Enter name to lookup(or press enter to finish) :")
    if name == "":
      break
    if name not in phonebook:
      print("Name not found")
    else:
      print(f" {name} -> {phonebook[name]}")

def main():
  print("01_phonebook")
  phonebook=read_phone_numbers()
  print_phonebook(phonebook)

  lookup_numbers(phonebook)

if __name__ == '__main__':
  main()
```

    01_phonebook
    Enter name: sara
    Enter number: 234235236
    Enter name: jawed
    Enter number: 544745
    Enter name: ali
    Enter number: 34788659
    Enter name: feroza
    Enter number: 2463657
    Enter name: 
    
     Phonebook: 
     sara -> 234235236
     jawed -> 544745
     ali -> 34788659
     feroza -> 2463657
    Enter name to lookup(or press enter to finish) :ali
     ali -> 34788659
    Enter name to lookup(or press enter to finish) :
    
