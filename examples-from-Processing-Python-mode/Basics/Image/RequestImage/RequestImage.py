"""
 * Request Image
 * by Ira Greenberg ( From Processing for Flash Developers).
 *
 * Shows how to use the request_image() function with preloader animation.
 * The request_image() function loads images on a separate thread so that
 * the sketch does not freeze while they load. It's very useful when you are
 * loading large images.
 *
 * These images are small for a quick download, but try it with your own huge
 * images to get the full effect.
 """

img_count = 12

image_promises = []

# Keeps track of loaded images (True or False)
load_states = []

def setup():
    size(640, 360)
    smooth()
    # Load images asynchronously
    for i in range(img_count):
        image_promises.append(request_image(Path('images') / f'PT_anim{i:04}.gif'))
        load_states.append(False)


def draw():
    background(0)
    # Start loading animation
    run_loader_ani()
    for i, img in enumerate(image_promises):
        # Check if individual images are fully loaded
        if img.is_ready:
            # As images are loaded set True in boolean array
            load_states[i] = True
    # When all images are loaded draw them to the screen
    if all(load_states):
        draw_images()


def draw_images():
    y = (height - image_promises[0].result.height) / 2
    img_width = width / len(image_promises)
    for i, img_promise in enumerate(image_promises):
        img = img_promise.result
        image(img, img_width * i, y, img.width, img.height)

# Loading animation
loader_x, loader_y = 0, 0
theta = 0

def run_loader_ani():
    global loader_x, loader_y, theta
    # Only run when images are loading
    if not all(load_states):
        ellipse(loader_x, loader_y, 10, 10)
        loader_x += 2
        loader_y = height / 2 + sin(theta) * (height / 8)
        theta += PI / 22
        # Reposition ellipse if it goes off the screen
        if loader_x > width + 5:
            loader_x = -5
