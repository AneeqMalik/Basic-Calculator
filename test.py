import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = subtract(4, 2)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = divide(8, 4)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
