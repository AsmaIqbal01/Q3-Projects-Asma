```python

def make_sentence(word,part_of_speech):
  if part_of_speech == 0:
    # word is a noun
    print("I am excited to add this "+ word + " to my vast collection of them!")
  elif part_of_speech == 1:
    # word is a verb
    print("It's so nice outside today it makes me want to " + word + "!")
  elif part_of_speech == 2:
    # word is adjective
    print("Looking out my window, the sky is big and " + word + "!")
  else:
    # part of speech is invalid
    print("Part of speech must be 0, 1, or 2! Can't make a sentence.")


def main():
  print("09_sentence_generator")
  word:str = input("Please type a noun, verb or an adjective:  ")
  print("Is this a noun ,verb or adjective? ")
  part_of_speech:int = int(input("Type 0 for noun, 1 for verb, 2 for adjective:  "))
  make_sentence(word,part_of_speech)

if __name__ == "__main__":
  main()
```

    09_sentence_generator
    Please type a noun, verb or an adjective:  bag
    Is this a noun ,verb or adjective? 
    Type 0 for noun, 1 for verb, 2 for adjective:  0
    I am excited to add this bag to my vast collection of them!
    
