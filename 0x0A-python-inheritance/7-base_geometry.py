#!/usr/bin/python3
class BaseGeometry:
    """
    class BaseGeometry.
    """
    def area(self):
        """
        public instance method: def area(self): raises
        Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: validator
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
