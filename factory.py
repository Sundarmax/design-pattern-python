class ShapeInterface:
    def draw(self):  pass

class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")

class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")

class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'Circle':
            return Circle()
        if type == 'Square':
            return Square()
