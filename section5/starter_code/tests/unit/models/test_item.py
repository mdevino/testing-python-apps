'''
Unit tests for ItemModel class.
'''

from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        actual = ItemModel('Something', 66.66)

        self.assertEqual(actual.name, 'Something')
        self.assertEqual(actual.price, 66.66)

    def test_item_json(self):
        actual = ItemModel('Something', 66.66)
        expected = {
            'name': 'Something',
            'price': 66.66
        }

        self.assertEqual(actual.json(), expected)