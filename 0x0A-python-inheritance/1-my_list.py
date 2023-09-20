#!/usr/bin/python3
class MyList(list):
    """
   inherits from list
    """
    def print_sorted(self):
        """
        Public instance method: prints list,
        but sorted (ascending)
        """
        print(sorted(self))
