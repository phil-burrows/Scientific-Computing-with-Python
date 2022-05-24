class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    attributes = f"Rectangle(width={self.width}, height={self.height})"
    return attributes

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    w = self.width
    h = self.height
    area = w * h
    return area

  def get_perimeter(self):
    w = self.width
    h = self.height
    perimeter = 2 * w + 2 * h
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    if self.height > 50:
      return "Too big for picture."
    elif self.width > 50:
      return "Too big for picture."
    else:
      picture = ''
      nline = "*"*self.width + "\n"
      picture += nline*self.height
      return picture

  def get_amount_inside(self, other):
    width_contains = self.width // other.width
    height_contains = self.height // other.height
    return width_contains * height_contains

class Square(Rectangle):

  def __init__(self, length):
    super().__init__(length, length)

  def __str__(self):
    return f'Square(side={self.width})'
  
  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side