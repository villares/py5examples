"""
Double Random
by Ira Greenberg.

Using two random() calls and the point() function
to create an irregular sawtooth line.
"""

total_pts = 300
steps = total_pts + 1


def setup():
    size(640, 360)
    stroke(255)
    frame_rate(1)


def draw():
    background(0)
    rand = 0
    for i in range(steps):
        point((width / steps) * i, (height / 2) + random(-abs(rand), abs(rand)))
        rand += random(-5, 5)
