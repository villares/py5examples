"""
Patterns.

Move the cursor over the image to draw with a software tool
which responds to the speed of the mouse.
"""


def setup():
    size(640, 360)
    background(102)


def draw():
    # Call the variableEllipse() method and send it the
    # parameters for the current mouse position
    # and the previous mouse position
    variable_ellipse(mouse_x, mouse_y, pmouse_x, pmouse_y)

# The simple method variableEllipse() was created specifically
# for this program. It calculates the speed of the mouse
# and draws a small ellipse if the mouse is moving slowly
# and draws a large ellipse if the mouse is moving quickly.


def variable_ellipse(x, y, px, py):
    speed = abs(x - px) + abs(y - py)
    stroke(speed)
    ellipse(x, y, speed, speed)