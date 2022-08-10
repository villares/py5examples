"""
BeginEndContour

This example shows how to cut a shape out of another using begin_contour() and end_contour().
"""


def setup():
    size(640, 360, P2D)
    smooth()
    # Make a shape
    global s
    s = create_shape()
    s.begin_shape()
    s.fill(0)
    s.stroke(255)
    s.stroke_weight(2)
    # Exterior part of shape, clockwise winding
    s.vertex(-100, -100)
    s.vertex(100, -100)
    s.vertex(100, 100)
    s.vertex(-100, 100)
    # Interior part of shape, counter-clockwise winding
    s.begin_contour()
    s.vertex(-10, -10)
    s.vertex(-10, 10)
    s.vertex(10, 10)
    s.vertex(10, -10)
    s.end_contour()
    # Finishing off shape
    s.end_shape(CLOSE)


def draw():
    background(52)
    # Display shape
    translate(width / 2, height / 2)
    # Shapes can be rotated
    s.rotate(0.01)
    shape(s)