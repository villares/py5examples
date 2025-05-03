"""
Color Variables (Homage to Albers).

This example creates variables for colors that may be referred to
in the program by a name, rather than a number.
"""
size(640, 360)
no_stroke()
background(51, 0, 0)

inside = color(204, 102, 0)
middle = color(204, 153, 0)
outside = color(153, 51, 0)
# Using hexadecimal notation between quotes, starting with #, is also possible.
# You may use the format you prefer.
#inside = '#CC6600'
#middle = '#CC9900'
#outside ='#993300'

with push_matrix():
    translate(80, 80)
    fill(outside)
    rect(0, 0, 200, 200)
    fill(middle)
    rect(40, 60, 120, 120)
    fill(inside)
    rect(60, 90, 80, 80)
with push_matrix():
    translate(360, 80)
    fill(inside)
    rect(0, 0, 200, 200)
    fill(outside)
    rect(40, 60, 120, 120)
    fill(middle)
    rect(60, 90, 80, 80)
