#!/usr/bin/python3
""" Shebang """


class Student:
    """
    Represents a student with first name, last name, and age.

    Public instance attributes:
    - first_name: The first name of the student.
    - last_name: The last name of the student.
    - age: The age of the student.

    Methods:
    - to_json(): Retrieves a dictionary representation of the Student instance.

    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
        - first_name: The first name of the student.
        - last_name: The last name of the student.
        - age: The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
        - A dictionary containing the attributes of the Student instance.

        """
        return self.__dict__
