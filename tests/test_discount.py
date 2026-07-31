import unittest

from src.discount import final_price


class DiscountTests(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(final_price(100, 0), 100)

    def test_ten_percent_discount(self):
        self.assertEqual(final_price(100, 0.1), 90)


class DiscountTests(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(final_price(100, 0), 100)

    def test_ten_percent_discount(self):
        self.assertEqual(final_price(100, 0.1), 90)

class DiscountTests(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(final_price(100, 0), 100)

    def test_ten_percent_discount(self):
        self.assertEqual(final_price(100, 0.1), 90)
class DiscountTests(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(final_price(100, 0), 100)

    def test_ten_percent_discount(self):
        self.assertEqual(final_price(100, 0.1), 90)

if __name__ == "__main__":
    unittest.main()


#我是你爸爸