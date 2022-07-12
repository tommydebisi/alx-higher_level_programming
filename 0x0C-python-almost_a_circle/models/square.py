#!/usr/bin/python3
"""
    square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializing special method

            Args:
                size: sixe of square
                x: coordinate x
                y: coordinate y
                id: number of objects created
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self) -> str:
        """
            string representation special method

            Returns:
                string representation of object
        """
        line = '[{}] ({}) {}/{} - {}'
        idd, xx, yy, si = self.id, self.x, self.y, self.__size

        return line.format(self.__class__.__name__, idd, xx, yy, si)

    @property
    def size(self):
        """
            gets the custom size
        """
        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            updates the square instance
        """
        i = 0
        if len(args) != 0:
            if len(args) == 1:  # only one arg to set
                setattr(self, "id", args[0])
                return

            for num, key in enumerate(self.__dict__.keys()):
                try:
                    if num == 0:
                        self.__dict__[key] = args[1]
                        continue
                    if num == 3:
                        i -= 1

                    self.__dict__[key] = args[i]
                    i += 1
                except IndexError:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            returns the dictionary representation of a Square
        """
        to_dic = dict()
        size_dic = dict()
        attr_names = ['size', 'id', 'x', 'y']
        i = 0
        for num, val in enumerate(self.__dict__.values()):
            if num == 2 or num == 3:
                continue
            if num == 1:
                size_dic[attr_names[i]] = val
                i += 1
                continue
            to_dic[attr_names[i]] = val
            i += 1
        size_dic.update(to_dic)

        return size_dic
