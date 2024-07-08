# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# Koch Curve
# A class to describe one line segment in the fractal.
# Includes methods to calculate midPy5Vectors along the line according to
# the Koch algorithm.


class KochLine(object):

    def __init__(self, start, end):
        # Two Py5Vectors,
        # a is the "left" Py5Vector and
        # b is the "right Py5Vector
        self.a = start.get()
        self.b = end.get()

    def display(self):
        stroke(255)
        line(self.a.x, self.a.y, self.b.x, self.b.y)

    def start(self):
        return self.a.get()

    def end(self):
        return self.b.get()

    # This is easy, just 1/3 of the way
    def kochleft(self):
        v = self.b - self.a
        v /= 3
        v += self.a
        return v

    # More complicated, have to use a little trig to figure out where this
    # Py5Vector is!
    def kochmiddle(self):
        v = self.b - self.a
        v /= 3
        p = self.a.get()
        p += v
        v.rotate(-radians(60))
        p += v
        return p

    # Easy, just 2/3 of the way
    def kochright(self):
        v = self.a - self.b
        v /= 3
        v += self.b
        return v
