# Object Oriented Programming boot.dev

## Classes

- Do not repeat yourself (DRY)
- Constructor (__init__)
- Instance variables is better than class variables

```python
# Class variable:
class Dragon:
    # Dragon class!
    element = "ice"

    def __init__(self, element):
```

```python
# Instance variable
class Dragon:
    # Dragon class!
    def __init__(self, element):
        self.element = element
```

## Encapsulation

Encapsulation is used to hide complex parts of the internal source code away from the main program
in order to organize and protect the internal parts of the program

- Organizes the code by moving complexity outside of the main program
- Protect internal data from public facing parts
- Hides complexity, lowers the barrier to entry for the project

```python
acceleration = calc_acceleration(initial_speed, final_speed, time)
```

- Encapsulation is _not_ security, it's for code organization

## Abstraction

Abstraction aims to provide an interface that exposes only the essential parts of a complex program, hiding the underlying implementation details to simplify interaction and reduce complexity.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
rect = Rectangle(10, 20)
print(f"Area: {rect.area()}")
```

Abstract Base Class (Shape): Defines the abstract method area(), providing an interface without implementation details.

Concrete Class (Rectangle): Implements the area() method, providing the specific behavior for calculating the area of a rectangle.

Interface Exposure: Users interact with the Shape interface (area() method), abstracting away the implementation details.

## Inheritance

Inheritance combats code reuse (DRY) by defining a general parent (or super) class
and an inherited child class that inherits some aspects of the parent

- Classes can be Parent -> Child
- Child class should have strict subset of its parent
- Wide inheritance is better than deep

```python
# Inheritance syntax in python
class Character:
    # Character class
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name

class Undead(Character):
    # Undead class
    def __init__(self, gender, name, hairstyle, facestyle):
        # reuses the `Character` class constructor
        # selects the gender and name properties
        super().__init__(gender, name)
        self.hairstyle = hairstyle
        self.facestyle = facestyle

# Example usage
make_imba_mage = Undead("Male", "Vurtne", "Straight sides", "Dead")
print(f"Name: {make_imba_mage.name}, Gender: {make_imba_mage.gender}, Hairstyle: {make_imba_mage.hairstyle}, Facestyle: {make_imba_mage.facestyle}")
```

## Polymorphism

Polymorphisism's core aspect is that an object can take many forms

- Poly = Many
- Morph = Form
- A class method () can be named the same (move) but output can take many forms

```python
class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")
```
