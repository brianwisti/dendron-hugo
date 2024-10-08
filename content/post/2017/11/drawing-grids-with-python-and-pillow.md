---
aliases:
- /2017/11/24/drawing-grids-with-python-and-pillow/
created: '2024-02-25 05:55:36'
date: 2017-11-24 00:00:00+00:00
description: ''
fname: pub.post.2017.11.drawing-grids-with-python-and-pillow
id: ac93a4rywy5wez6nk7r5c1w
slug: drawing-grids-with-python-and-pillow
tags:
- python
- programming
title: Drawing Grids with Python and Pillow
updated: '2024-08-07 18:49:02'
---

![line drawing superimposed over a grid of small squares](assets/img/2017/cover-2017-11-24.png)

Hey I used [Python]({{< relref "/card/python.md" >}}) and [Pillow](https://python-pillow.org/) to make grids for my drawing. Read on to watch my brain while I figured it out. Apologies for the minimal editing and the ridiculous number of images.

I enjoy drawing. Many of my sketches have repeated elements, like Zentangle or Celtic inspired patterns. Okay, I don’t have many examples on the site. Sure there’s plenty of repetition based on symmetry tools in the drawing apps I use, and a little bit taking advantage of perspective grids. Not much in the way of simple grid-based repetition though.

Templates exist, but I want custom templates to fit the size of my workspace. I started exploring the Pillow library recently, so let’s use that to make custom grids for my drawings.

``` python
from PIL import Image

if __name__ == '__main__':
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    image.show()
```

I use a modest 600 by 600 pixel grayscale image while working out the details. No point saving anything until I know what’s going on, so just `show()` the image.

![A blank image](assets/img/2017/grid-blank.png)

Most of what I want is in the [ImageDraw](http://pillow.readthedocs.io/en/4.3.x/reference/ImageDraw.html) module.

## Simple Grid

```python
from PIL import Image, ImageDraw

if __name__ == '__main__':
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw a line
    draw = ImageDraw.Draw(image)
    x = image.width / 2
    y_start = 0
    y_end = image.height
    line = ((x, y_start), (x, y_end))
    draw.line(line, fill=128)
    del draw

    image.show()
```

![Drawing one line](assets/img/2017/grid-single-line.png)

Nice. Okay, how about repeating some lines across?

``` python
from PIL import Image, ImageDraw

if __name__ == '__main__':
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / 10)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    del draw

    image.show()
```

![Drawing some columns](assets/img/2017/grid-columns.png)
Lovely. How about an actual grid?

```python
from PIL import Image, ImageDraw

if __name__ == '__main__':
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / 10)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    del draw

    image.show()
```

![Drawing a simple grid](assets/img/2017/grid-simple-grid.png)

Okay cool but I often need a specific number of squares in my grid.

```python
from PIL import Image, ImageDraw

if __name__ == '__main__':
    step_count = 25
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    del draw

    image.show()
```

![Specifying a step count](assets/img/2017/grid-step-count.png)

Right but I don’t want to edit the code every time.

```python
import sys

from PIL import Image, ImageDraw

if __name__ == '__main__':
    step_count = 10

    if len(sys.argv) == 2:
        step_count = int(sys.argv[1])

    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    del draw

    image.show()
```

Run it.

```bash
python grid.py 12
```

![Grabbing a step count from the command line](assets/img/2017/grid-specify-step-count.png)

I can specify step count from the command line. Cool. Uh hey about height and width?

```python
import sys

from PIL import Image, ImageDraw

if __name__ == '__main__':
    step_count = 10
    height = 600
    width = 600

    if len(sys.argv) == 2:
        step_count = int(sys.argv[1])
    elif len(sys.argv) == 3:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    elif len(sys.argv) == 4:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        step_count = int(sys.argv[3])

    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    del draw

    image.show()
```

Oh come on. Stop it with `sys.argv`. Get some real command line handling in there.

``` python
import argparse

from PIL import Image, ImageDraw

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("width", help="width of image in pixels",
                        type=int)
    parser.add_argument("height", help="height of image in pixels",
                        type=int)
    parser.add_argument("step_count", help="how many steps across the grid",
                        type=int)
    args = parser.parse_args()

    step_count = args.step_count
    height = args.height
    width = args.width

    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    del draw

    image.show()
```

Much better. Run it.

```console
$ python grid.py
usage: grid.py [-h] width height step_count

positional arguments:
  width       width of image in pixels
  height      height of image in pixels
  step_count  how many steps across the grid

optional arguments:
  -h, --help  show this help message and exit

$ python grid.py 500 500 20
```

I like [Argparse](https://docs.python.org/3/library/argparse.html[Argparse]).

![Constructing grid from Argparse arguments](assets/img/2017/grid-specify-size-steps.png)

Anyways - what if I ask for a rectangle instead of a square?

```bash
python grid.py 400 600 24
```

![Rectangular grid](assets/img/2017/grid-rectangular.png "Rectangular grid")

Hold on. I was handing `height` and `width` to [Image](http://pillow.readthedocs.io/en/4.3.x/reference/Image.html#the-image-class) in the wrong order this whole time.

```python
if __name__ == '__main__':
    # ...

    image = Image.new(mode='L', size=(width, height), color=255)

    # ...
```

Run it.

```bash
python grid.py 400 600 24
```

![Correct Image initialization](assets/img/2017/grid-correct-image-init.png)

This works. I have half a dozen ideas left, but I want to use it for a sketch _now_.

**`grid.py`**

```python
import argparse

from PIL import Image, ImageDraw

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("width", help="width of image in pixels",
                        type=int)
    parser.add_argument("height", help="height of image in pixels",
                        type=int)
    parser.add_argument("step_count", help="how many steps across the grid",
                        type=int)
    args = parser.parse_args()

    step_count = args.step_count
    height = args.height
    width = args.width
    image = Image.new(mode='L', size=(width, height), color=255)

    # Draw a grid
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    del draw

    filename = "grid-{}-{}-{}.png".format(width, height, step_count)
    print("Saving {}".format(filename))
    image.save(filename)
```

```console
$ python grid.py 1800 2400 50
Saving grid-1800-2400-50.png
$ ls
grid-1800-2400-50.png   grid.py*
```

Let’s skim over the part where I get the grid onto the iPad and import it as a new layer in my current sketch. That part includes no code — for now.

Anyways, back to the sketch.