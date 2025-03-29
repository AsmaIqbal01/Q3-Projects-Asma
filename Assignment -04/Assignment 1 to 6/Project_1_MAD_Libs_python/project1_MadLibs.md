```python
def main():
  print("Project 1---MadLibs Python Project")
  story_templates=(
       "In a {place}, there lived a {adjective} {animal}. "
        "Every day, the {animal} would {verb} in the {place} and make everyone {emotion}. "
        "One day, it found a {adjective2} {object} and decided to {verb2} with it."
    )
  #Collect words from users
  print("Welcome to Mad Libs! Please provide the following words:")
  place:str=str(input("Enter a place:"))
  adjective:str=str(input("Enter an adjective:"))
  animal:str=str(input("Enter an animal:"))
  verb:str=str(input("Enter a verb:"))
  emotion:str=str(input("Enter an emotion:"))
  object:str=str(input("Enter an object:"))
  adjective2:str=str(input("Enter an adjective:"))
  verb2:str=str(input("Enter a verb:"))

  story:str=story_templates.format(
      place=place,
      adjective=adjective,
      animal=animal,
      verb=verb,
      emotion=emotion,
      object=object,
      adjective2=adjective2,
      verb2=verb2
  )
  print(f"Here is your final mad libs story : \n {story}")
if __name__ == '__main__':
  main()
```

    Project 1---MadLibs Python Project
    Welcome to Mad Libs! Please provide the following words:
    Enter a place:forest
    Enter an adjective:shinny
    Enter an animal:cat
    Enter a verb:run
    Enter an emotion:happy
    Enter an object:ball
    Enter an adjective:smart
    Enter a verb:swing
    Here is your final mad libs story : 
     In a forest, there lived a shinny cat. Every day, the cat would run in the forest and make everyone happy. One day, it found a smart ball and decided to swing with it.
    
