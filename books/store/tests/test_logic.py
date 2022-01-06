from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(14, 13, '-')
        self.assertEqual(1, result)

    def test_multiply(self):
        result = operations(4, 2, '*')
        self.assertEqual(8, result)

    def test_division(self):
        result = operations(9, 3, '/')
        self.assertEqual(3, result)

    def test_int_division(self):
        result = operations(9, 4, '//')
        self.assertEqual(2, result)