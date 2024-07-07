from abc import ABC, abstractmethod

# Visitor Interface
class DiscountVisitor(ABC):
    @abstractmethod
    def visit_food(self, food):
        pass

    @abstractmethod
    def visit_clothing(self, clothing):
        pass

    @abstractmethod
    def visit_electronics(self, electronics):
        pass

# Concrete Visitors
class HolidayDiscountVisitor(DiscountVisitor):
    def visit_food(self, food):
        print("Applying holiday discount to food")

    def visit_clothing(self, clothing):
        print("Applying Holiday disocount to clothing")

    def visit_electronics(self, electronics):
        print("Applying holiday discount to electornics")


class ClearanceDiscountVisitor(DiscountVisitor):
    def visit_food(self, food):
        print("Applying Clearancediscount to food")

    def visit_clothing(self, clothing):
        print("Applying Clearance discount to clothing")

    def visit_electronics(self, electronics):
        print("Applying Clearance discount to electronics")


# Product Interface
class Product(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Products
class Food(Product):
    def accept(self, visitor):
        visitor.visit_food(self)

class Clothing(Product):
    def accept(self, visitor):
        visitor.visit_clothing(self)

class Electronics(Product):
    def accept(self, visitor):
        visitor.visit_electronics(self)


# Usage
food = Food()
clothing = Clothing()
electronics = Electronics()

holiday_visitor =  HolidayDiscountVisitor()
cleareance_visitor = ClearanceDiscountVisitor()

food.accept(holiday_visitor)
clothing.accept(cleareance_visitor)
electronics.accept(holiday_visitor)



# Output
# Applying holiday discount to food
# Applying Clearance discount to clothing
# Applying holiday discount to electornics
