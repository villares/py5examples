"""
Redraw.

The redraw() function makes draw() execute once.
In this example, draw() is executed once every time
the mouse is clicked.
"""

y = 180


def setup():
    """
    The statements in the setup() function
    execute once when the program begins.
    """
    size(640, 360)    # Size should be the first statement
    stroke(255)         # Set line drawing color to white
    no_loop()


def draw():
    """
    The statements in draw() are executed until the
    program is stopped. Each statement is executed in
    sequence and after the last line is read, the first
    line is executed again.
    """
    global y
    background(0)     # Set the background to black
    y = y - 4
    if (y < 0):
        y = height
    line(0, y, width, y)


def mouse_pressed():
    redraw()
