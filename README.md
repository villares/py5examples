# py5 Examples

![py5 logo](images/logo.png)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/py5coding/py5examples/HEAD?urlpath=lab)

[![py5 downloads](https://pepy.tech/badge/py5/month)](https://pepy.tech/project/py5)

[![Downloads](https://pepy.tech/badge/py5/week)](https://pepy.tech/project/py5)

py5 is a new version of [**Processing**][processing] for Python 3.8+. It makes the Java [**Processing**][processing] jars available to the CPython interpreter using [**JPype**][jpype]. It can do just about all of the 2D and 3D drawing [**Processing**][processing] can do, except with Python instead of Java code.

The goal of py5 is to create a new version of Processing that is integrated into the Python ecosystem. Built into the library are thoughtful choices about how to best get py5 to work with other popular Python libraries and tools such as [Jupyter][jupyter], [numpy][numpy], and [Pillow][pillow].

Here is a simple example of a working py5 Sketch, written in module mode:

``` python
import py5


def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)


py5.run_sketch()
```

If you have Java 11 installed on your computer, you can install py5 using pip:

``` bash
pip install py5
```

[Detailed installation instructions](https://py5coding.org/content/install.html) are available on the documentation website. There are some [Special Notes for Mac Users](https://py5coding.org/content/osx_users.html) that you should read if you use OSX.

There are currently four basic ways to use py5. They are:

* **module mode**, as shown above
* **class mode**: create a Python class inherited from `py5.Sketch`, and support multiple Sketches running at the same time.
* **imported mode**: simplified code that omits the `py5.` prefix. This mode is supported by the py5 Jupyter notebook kernel and the `run_sketch` command line utility.
* **static mode**: functionless code to create static images. This mode is supported by the py5bot Jupyter notebook kernel and the `%%py5bot` IPython magic.

py5generator is a meta-programming project that creates the py5 library. To view the actual installed py5 library code, look at the [py5 repository][py5_repo]. All py5 library development is done through py5generator.

The documentation website, [https://py5coding.org/](https://py5coding.org/), is very much a work in progress. The reference documentation is solid but the how-to's and tutorials need a lot of work.

[py5_repo]: https://github.com/py5coding/py5
[processing]: https://github.com/processing/processing4
[jpype]: https://github.com/jpype-project/jpype

[jupyter]: https://jupyter.org/
[numpy]: https://numpy.org/
[pillow]: https://python-pillow.org/
