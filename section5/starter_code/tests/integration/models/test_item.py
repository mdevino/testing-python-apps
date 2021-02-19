from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Something', 12.34)

            self.assertIsNone(ItemModel.find_by_name('Something'))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('Something'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('Something'))