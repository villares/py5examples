# companion to AnimatedScrite.py

# Class for animating a sequence of GIFs
from pathlib import Path
from py5 import *

class Animation(object):

    def __init__(self, image_prefix, count, images_folder='images'):
        self.frame = 0
        self.image_count = count
        self.images = []
        for i in range(self.image_count):
            # Use f'{i:04}' to format i into four digits
            filename = Path(images_folder) / f'{image_prefix}{i:04}.gif'
            self.images.append(load_image(filename))

    def display(self, xpos, ypos):
        self.frame = (self.frame + 1) % self.image_count
        image(self.images[self.frame], xpos, ypos)

    def get_width(self):
        return self.images[0].width
