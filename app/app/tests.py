from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """
        Tests that two numbers are addded together
        """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """
        Tests that two numbers are subtracted
        """
        self.assertEqual(subtract(5, 11), 6)
