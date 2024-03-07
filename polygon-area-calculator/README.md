# Polygon Area Calculator

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle, and inherit its methods and attributes.

## Rectangle class

When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

- `set_width`<br>
- `set_height`<br>
- `get_area`: Returns area (`width` * `height`)<br>
- `get_perimeter`: Returns perimeter (2 * `width` + 2 * `height`)<br>
- `get_diagonal`: Returns diagonal ((`width` ** 2 + `height` ** 2) ** .5)<br>
- `get_picture`: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
- `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`

## Square class

The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__` method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

Additionally, the set_width and set_height methods on the Square class should set both the width and height.


## Usage example

`rect = Rectangle(10, 5)`<br>
`print(rect.get_area())`<br>
`rect.set_height(3)`<br>
`print(rect.get_perimeter())`<br>
`print(rect)`<br>
`print(rect.get_picture())`<br>

`sq = Square(9)`<br>
`print(sq.get_area())`<br>
`sq.set_side(4)`<br>
`print(sq.get_diagonal())`<br>
`print(sq)`<br>
`print(sq.get_picture())`<br>

`rect.set_height(8)`<br>
`rect.set_width(16)`<br>
`print(rect.get_amount_inside(sq))`<br>

That code should return:

`50`<br>
`26`<br>
`Rectangle(width=10, height=3)`<br>
`**********`<br>
`**********`<br>
`**********`<br>

`81`<br>
`5.656854249492381`<br>
`Square(side=4)`<br>
`****`<br>
`****`<br>
`****`<br>
`****`<br>

`8`<br>
