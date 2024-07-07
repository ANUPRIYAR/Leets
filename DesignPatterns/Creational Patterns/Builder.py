# Product class
class Pizza:
    def __init__(self, size='default', crust="default", toppings="default"):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def show_pizza(self):
        print(f"Pizza Size:{self.size} , Crust:{self.crust}, toppings: {self.toppings}")


# Abstract Builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_size(self): pass
    def build_crust(self): pass
    def build_toppings(self): pass


# Concrete Builder
class HawaiianPizzaBuilder(PizzaBuilder):
    def build_size(self):
        self.pizza.size = "Large"

    def build_crust(self):
        self.pizza.crust = "Thin"

    def build_toppings(self):
        self.pizza.toppings = "chicken sausage"


# Director
class Waiter:
    def __init__(self, pizza_builder):
        self.pizza_builder = pizza_builder

    def construct_pizza(self):
        self.pizza_builder.build_size()
        self.pizza_builder.build_crust()
        self.pizza_builder.build_toppings()

    def get_pizza(self):
        return self.pizza_builder.pizza


# Client code
if __name__ == "__main__":
    waiter = Waiter(HawaiianPizzaBuilder())
    waiter.construct_pizza()
    pizza = waiter.get_pizza()
    pizza.show_pizza()



# Pizza Size:Large , Crust:Thin, toppings: chicken sausage