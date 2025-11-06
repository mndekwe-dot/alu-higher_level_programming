#!/usr/bin/python3
"""Module that defines a Square class with position"""


class Square:
    """Class that defines a square with size, position, area, and printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance

        Args:
            size: The size of the square (default: 0)
            position: The position offset for printing (default: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size attribute

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute with validation

        Args:
            value: The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueE
