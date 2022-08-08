"""
Image Mask

Move the mouse to reveal the image through the dynamic mask.
"""

mask_shader = None
src_image = None
mask_image = None


def setup():
    global mask_shader, src_image, mask_image
    size(640, 360, P2D)
    src_image = load_image("leaves.jpg")
    mask_image = create_graphics(src_image.width, src_image.height, P2D)
    mask_image.no_smooth()
    mask_shader = load_shader("mask.glsl")
    mask_shader.set("mask", mask_image)
    background(255)


def draw():
    mask_image.begin_draw()
    mask_image.background(0)
    if mouse_x != 0 and mouse_y != 0:
        mask_image.no_stroke()
        mask_image.fill(255, 0, 0)
        mask_image.ellipse(mouse_x, mouse_y, 50, 50)
    mask_image.end_draw()
    shader(mask_shader)
    image(src_image, 0, 0, width, height)
