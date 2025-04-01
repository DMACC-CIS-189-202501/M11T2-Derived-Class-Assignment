class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):   
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address  