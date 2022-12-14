import unittest
from FizzBuzz import fizz_buzz


class FizzBuzzTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizz_buzz(range(1, 6))[0], "1")

    def test_2(self):
        self.assertEqual(fizz_buzz(range(1, 6))[1], "2")

    def test_3(self):
        self.assertEqual(fizz_buzz(range(1, 6))[2], "fizz")

    def test_4(self):
        self.assertEqual(fizz_buzz(range(1, 6))[3], "4")

    def test_5(self):
        self.assertEqual(fizz_buzz(range(1, 6))[4], "buzz")


if __name__ == '__main__':
    unittest.main()
