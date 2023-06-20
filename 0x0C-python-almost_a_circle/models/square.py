#!/usr/bin/python3
"""square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class basing on rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initilaise instnce"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overide str in rectangle"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        """gets size"""
        return self.height

    @size.setter
    def size(self, value):
        """sets value of size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """update value"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                else:
                    self.y = value

    def to_dictionary(self):
        """dictionary rep of square"""
        return {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y}
