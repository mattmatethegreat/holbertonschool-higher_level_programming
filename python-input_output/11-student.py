#!/usr/bin/python4
""" shebang """


class Student:
    """
    Represents a student with first name, last name, and age.

    Public instance attributes:
    - first_name: The first name of the student.
    - last_name: The last name of the student.
    - age: The age of the student.

    Methods:
    - to_json(attrs=None): Retrieves a dictionary
    representation of the Student instance.
    - reload_from_json(json): Replaces all attributes of the
    Student instance with values from the provided json dictionary.

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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
        - attrs: A list of attribute names to include in the 
        dictionary representation. Default is None.

        Returns:
        - A dictionary containing the attributes of the Student instance.

        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance 
        with values from the provided json dictionary.

        Args:
        - json: A dictionary containing attribute names 
        and their corresponding values.

        """
        for attr, value in json.items():
            setattr(self, attr, value)
