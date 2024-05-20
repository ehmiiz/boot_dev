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