#a = Vector2D(3, 4)
#b = Vector2D(8, -5)
#c = Vector2D(0, 4)

#a + b == Vector2D(11, -1)
#a + b + c == b + c + a
#a + -a == Vector2D(0, 0)
#c ** 0.5 == Vector2D(0, 2)
#abs(a) == 5
#No "strange" operations should be allowed

from math import hypot

class Vector2D():
        def __init__(self, x, y):
                self._x = x
                self._y = y

        def __repr__(self):
                return 'Vector2D({}, {})'.format(self._x, self._y)
        def __add__(self, other):
                if not isinstance(other, Vector2D):
                        return NotImplemented
                return Vector2D(self._x + other._x, self._y + other._y)
        def __eq__(self, other):
                if not isinstance(other, Vector2D):
                        return NotImplemented
                return self._x == other._x and self._y == other._y
        def __neg__(self):
                return Vector2D(-self._x, -self._y)
        def __pow__(self, num):
                x = self._x ** num
                y = self._y ** num
                return Vector2D(x, y)
        def __abs__(self):
                return hypot(self._x, self._y)
        #(self._x**2 + self._y**2)**0.5
        
        def __mul__(self, other):
                if not isinstance(other, (int, float)):
                        return NotImplemented
                return Vector2D(self._x * other, self._y * other)
        def __rmul__(self, other):
                return self * other
        @property
        def x(self):
                return self._x
        @property
        def y(self):
                return self._y

a = Vector2D(3, 4)
b = Vector2D(8, -5)
c = Vector2D(0, 4)

a.x, a.y


