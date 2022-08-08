"""
Random.

Random numbers create the basis of this image.
Each time the program is loaded the result is different.
"""


def setup():
    size(640, 360)
    background(0)
    stroke_weight(20)
    frame_rate(2)


def draw():
    for i in range(width):
        r = random(255)
        stroke(r)
        line(i, 0, i, height)
