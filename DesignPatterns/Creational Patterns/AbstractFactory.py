# Abstract Product Interfaces
class Drink:
    def serve(self):
        pass

class Pastry:
    def serve(self):
        pass

# Concrete Products
class CoffeeDrink(Drink):
    def serve(self):
        return "Serving coffee"

class CoffeePastry(Pastry):
    def serve(self):
        return "serving Croissant"

class TeaDrink(Drink):
    def serve(self):
        return "serving Tea"

class TeaPastry(Pastry):
    def serve(self):
        return "serving Scone"


#  Abstract Factory Interfaces
class CafeFactory:
    def createDrink(self):
        pass

    def createPastry(self):
        pass

# Concrete Factories
class CoffeCafeFactory(CafeFactory):
    def createDrink(self):
        return CoffeeDrink()

    def createPastry(self):
        return CoffeePastry()

class TeaCafeFactory(CafeFactory):
    def createDrink(self):
        return TeaDrink()

    def createPastry(self):
        return TeaPastry()


# Main
# Creating a coffee drink
coffee_factory = CoffeCafeFactory()
coffee = coffee_factory.createDrink()
croissant = coffee_factory.createPastry()

print(coffee.serve())
print(croissant.serve())


# Creating A Tea Caffe
tea_factory = TeaCafeFactory()
tea = tea_factory.createDrink()
scone = tea_factory.createPastry()

print(tea.serve())
print(scone.serve())



# Serving coffee
# serving Croissant
# serving Tea
# serving Scone