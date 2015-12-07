#a = Vector2D(3, 4)
#b = Vector2D(8, -5)
#c = Vector2D(0, 4)

#a + b == Vector2D(11, -1)
#a + b + c == b + c + a
#a + -a == Vector2D(0, 0)
#c ** 0.5 == Vector2D(0, 2)
#abs(a) == 5
#No "strange" operations should be allowed

class Vector2D():
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def __repr__(self):
                return 'Vector2D({}, {})'.format(self.x, self.y)
        def __add__(self, other):
                x = self.x + other.x
                y = self.y + other.y
                return Vector2D(x, y)
        def __neg__(self):
                return Vector2D(-self.x, -self.y)
        def __pow__(self, num):
                x = self.x ** num
                y = self.y ** num
                return Vector2D(x, y)
        def __abs__(self):
                return (self.x**2 + self.y**2)**0.5

a = Vector2D(3, 4)
b = Vector2D(8, -5)
c = Vector2D(0, 4)


