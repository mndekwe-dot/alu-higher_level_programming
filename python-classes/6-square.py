#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.
        Args:
            size (int): size of the square (default 0)
            position (tuple): position of the square (default (0, 0))
        """
        self.size = size
        self.position = position
