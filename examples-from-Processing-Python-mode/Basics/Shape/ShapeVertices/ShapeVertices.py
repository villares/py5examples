"""
Shape Vertices.

How to iterate over the vertices of a shape.
When loading an obj or SVG, get_vertex_count()
will typically return 0 since all the vertices
are in the child shapes.
You should iterate through the children and then
iterate through their vertices.
"""


def setup():
    size(640, 360)
    # Load the shape
    global uk
    uk = load_shape("uk.svg")


def draw():
    background(51)
    # Center where we will draw all the vertices
    translate(width / 2 - uk.get_width() / 2, height / 2 - uk.get_height() / 2)

    # Iterate over the children
    children = uk.get_child_count()
    for i in range(children):
        child = uk.get_child(i)
        total = child.get_vertex_count()

        # Now we can actually get the vertices from each child
        for j in range(total):
            v = child.get_vertex(j)
            # Cycling brightness for each vertex
            stroke((frame_count + (i + 1) * j) % 255)
            # Just a dot for each one
            point(v.x, v.y)
