""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication

class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, value_1):
        """ This is the add method"""
        self.result = self.result + value_1
        return self.result

    def subtract(self, value_1):
        """ This is the subtract method"""
        self.result = self.result - value_1
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
