# GLSL version of Conway's game of life, ported from GLSL sandbox:
# http://glsl.heroku.com/e#207.3
# Exemplifies the use of the ppixels uniform in the shader, that gives
# access to the pixels of the previous frame.

conway = None
pg = None


def setup():
    global conway, pg
    size(400, 400, P3D)
    conway = load_shader("conway.glsl")
    pg = create_graphics(400, 400, P2D)
    pg.no_smooth()
    conway.set("resolution", float(pg.width), float(pg.height))


def draw():
    conway.set("time", millis() / 1000.0)
    x = remap(mouse_x, 0, width, 0, 1)
    y = remap(mouse_y, 0, height, 1, 0)
    conway.set("mouse", x, y)
    pg.begin_draw()
    pg.background(0)
    pg.shader(conway)
    pg.rect(0, 0, pg.width, pg.height)
    pg.end_draw()
    image(pg, 0, 0, width, height)
