## Converting the Processing Python mode examples to py5

Processing IDE comes ready with a big collection of examples. In [Processing.py](https://py.processing.org) a.k.a Processing Python Mode you had almost all those examples ported/converted to Python. Now we want to have them working on py5!

### A first attempt, you can help!

This might still be a rough conversion, you can help by testing the examples and opening an issue!

Open an issue here if you find a broken example: https://github.com/villares/py5examples/issues

### How to run this code?

To run this, you'll need [py5](https://py5coding.org). I strongly suggest using [Thonny IDE](https://thonny.org) and the [thonny-py5mode](https://github.com/tabreturn/thonny-py5mode/) plugin. [Step by step instructions here](https://abav.lugaralgum.com/como-instalar-py5/index-EN.html).

To make these converted examples "look and feel" closer to the Processing & Processing Python mode examples, they are written mostly in the style of **imported mode**. We could have also a collection of **module mode** examples, and even **class mode**, etc. [Read about the py5 modes here](https://py5coding.org/content/py5_modes.html).

### Conversion notes

- This might need change in the future:

For secondary .py files of a sketch I have used this, which is not very nice:
`from py5 import *` 

Using *module mode*, a.k.a `import py5`, can be done but also has issues.
This has to be thought out better.

- Try some numpy optimization?

  - Basics/Math/Graphing2DEquation/Graphing2DEquation.py
  - There are some *noise* ideas being discussed here: https://github.com/py5coding/py5generator/discussions/232

- Not good yet:

  - Topics/Create Shapes/ParticleSystemPShape/ParticleSystemPShape.py
