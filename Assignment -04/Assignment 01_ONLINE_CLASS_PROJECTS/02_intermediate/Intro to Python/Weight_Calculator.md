```python
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def mars_weight():
    print("Milestone-1: Mars Weight")
    weight_on_earth = float(input("Enter weight on Earth : "))
    weight_on_mars = weight_on_earth * GRAVITY_FACTORS["Mars"]
    print(f"Weight on Mars: {weight_on_mars:.2f}")

def planetary_weight():
    print("Milestone-2: Planet Weight")
    planet_to_weight = input("Enter planet name: ").capitalize()
    weight_on_earth = float(input("Enter weight on Earth: "))

    if planet_to_weight in GRAVITY_FACTORS:
        weight_on_planet = weight_on_earth * GRAVITY_FACTORS[planet_to_weight]
        print(f"Weight on {planet_to_weight}: {weight_on_planet:.2f}")
    else:
        print("Invalid planet name. Please enter a valid planet from the list.")

def main():
    print("Planetary Weight Calculator!")
    print("-----------------------------------")
    mars_weight()
    planetary_weight()
if __name__ == '__main__':
    main()
```

    Planetary Weight Calculator!
    -----------------------------------
    Milestone-1: Mars Weight
    Enter weight on Earth : 140
    Weight on Mars: 52.92
    Milestone-2: Planet Weight
    Enter planet name: Uranus
    Enter weight on Earth: 120
    Weight on Uranus: 97.80
    
