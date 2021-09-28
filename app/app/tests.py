from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):

        self.assertEqual(subtract(5, 11), 6)
