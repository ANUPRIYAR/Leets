from copy import deepcopy

# Prototype
class Car:
    def __init__(self):
        self.model = 'Basic'
        self.color = 'White'

    def clone(self):
        return deepcopy(self)

    def customize(self, color, accessories):
        raise NotImplementedError


# Concrete Car
class BasicCar(Car):
    def customize(self, color, accessories):
        self.color = color
        print(f"Car customized with color {self.color} and accessories {accessories}")


# Client code
if __name__== "__main__":
    basiccar = BasicCar()
    customercar = basiccar.clone()

    customercar.customize("Red", "Sunroof")


# Car customized with color Red and accessories Sunroof

# If we remove the cusotmize method from BasicCar class, then while running it will
#     raise NotImplementedError
# NotImplementedError