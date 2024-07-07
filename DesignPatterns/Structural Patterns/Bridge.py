# Implementor
class Transmission:
    def apply_gear(self):
        pass

# Concrete Implementation
class ManualTransmission(Transmission):
    def apply_gear(self):
        print("Manual Transmission applied")

class AutomaticTransmission(Transmission):
    def apply_gear(self):
        print("Automatic transmission applied")


# Abstraction
class Vehicle:
    def __init__(self, transmission):
        self.transmission = transmission

    def apply_transmission(self):
        pass


# Refined Abstraction
class Car(Vehicle):
    def apply_transmission(self):
        self.transmission.apply_gear()

# Refined Abstraction
class Truck(Vehicle):
    def apply_transmission(self):
        self.transmission.apply_gear()


# Client code
manual = ManualTransmission()
car = Car(manual)
car.apply_transmission()

# Manual Transmission applied