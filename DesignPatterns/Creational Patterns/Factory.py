class Shape:
    def draw(self):
        pass

# concerete class 1
class Hexagon(Shape):
    def draw(self):
        print("Drawing a Hexagon")

#  Concerete class 2
class Pentagon(Shape):
    def draw(self):
        print("Drawing Pentagon")

# Factory class
class ShapeFactory:
    @staticmethod
    def get_shape(type):
        if type == 'Hexagon':
            return Hexagon()
        elif type == 'Pentagon':
            return Pentagon()
        else:
            return None

# Client Code
if __name__ == "__main__":
    hexa = ShapeFactory.get_shape('Hexagon')
    hexa.draw()

    penta = ShapeFactory.get_shape('Pentagon')
    penta.draw()



# Drawing a Hexagon
# Drawing Pentagon